#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define img_height 512
#define img_width 512
#define gray_level 256
#define raw_path "../images/lab1(512x512x8bit).raw"
#define bmp_path "../images/lab1(512x512x8bit).bmp"

typedef uint8_t BYTE; // 1BYTE = 8b
typedef uint16_t WORD; // 1WORD = 2BYTE = 16b
typedef uint32_t DWORD; // 1DWORD = 4BYTE = 32b
typedef int32_t LONG; // LONG占用的字节数与DWORD相同，但LONG的最高一位为符号位

typedef struct __attribute__((packed)) tagBITMAPFILEHEADER {
    WORD bfType;//文件类型，必须是0x424D,即字符“BM”
    DWORD bfSize;//文件大小
    WORD bfReserved1;//保留字
    WORD bfReserved2;//保留字
    DWORD bfOffBits;//从文件头到实际位图数据的偏移字节数
} BITMAPFILEHEADER;//位图文件头

typedef struct __attribute__((packed)) tagBITMAPINFOHEADER {
    DWORD biSize;//信息头大小
    LONG biWidth;//图像宽度
    LONG biHeight;//图像高度
    WORD biPlanes;//位平面数，必须为1
    WORD biBitCount;//每像素位数
    DWORD biCompression;//压缩类型
    DWORD biSizeImage;//压缩图像大小字节数
    LONG biXPelsPerMeter;//水平分辨率
    LONG biYPelsPerMeter;//垂直分辨率
    DWORD biClrUsed;//位图实际用到的色彩数
    DWORD biClrImportant;//本位图中重要的色彩数
} BITMAPINFOHEADER;//位图信息头

typedef struct __attribute__((packed)) tagRGBQUAD {
    BYTE rgbBlue;
    BYTE rgbGreen;
    BYTE rgbRed;
    BYTE rgbReserved;
} RGBQUAD;

int main() {
    printf("=======================================\n"
           "Running raw2bmp created by Kilo A. FENG\n"
           "=======================================\n");

    BITMAPFILEHEADER bmp_fh; //BMP file header
    BITMAPINFOHEADER bmp_ih; //BMP info header
    RGBQUAD rgb[gray_level];
    uint32_t counter[gray_level];
    uint32_t intensity;
    int row_size = ((8 * img_width) + 31) / 32 * 4; //bytes
    int pixel_array_size = row_size * abs(img_height); //bytes

    //open raw file
    FILE *raw_fp = fopen(raw_path, "rb");
    if (raw_fp == NULL) {
        printf("Failed to open raw file\n");
        exit(0);
    } else printf("Raw file opened\n");

    //apply memory for raw data
    unsigned char *raw = calloc(img_height, img_width);
    if (raw == NULL) {
        printf("Failed to apply memory for raw data\n");
        exit(0);
    }
    printf("Memory applied for raw data\n");

    fread(raw, sizeof(BYTE), img_height * img_width, raw_fp);
    printf("Raw data written in memory\n");
    fclose(raw_fp); //close raw file
    printf("Raw file closed\n");


    //generate palette
    for (int i = 0; i < gray_level; ++i) {
        rgb[i].rgbRed = i;
        rgb[i].rgbGreen = i;
        rgb[i].rgbBlue = i;
        rgb[i].rgbReserved = 0;
    }

    //generate info header
    {
        bmp_ih.biSize = 40;
        bmp_ih.biWidth = row_size;
        bmp_ih.biHeight = img_height;
        bmp_ih.biPlanes = 1;
        bmp_ih.biBitCount = 8; //256灰度级
        bmp_ih.biCompression = 0;
        bmp_ih.biSizeImage = pixel_array_size;
        bmp_ih.biXPelsPerMeter = 0;
        bmp_ih.biYPelsPerMeter = 0;
        bmp_ih.biClrUsed = 0;
        bmp_ih.biClrImportant = 0;
    }

    //generate file header
    {
        bmp_fh.bfType = 0x4D42;
        bmp_fh.bfSize = bmp_fh.bfOffBits + pixel_array_size;
        bmp_fh.bfReserved1 = 0;
        bmp_fh.bfReserved2 = 0;
        bmp_fh.bfOffBits = sizeof(bmp_fh) + sizeof(bmp_ih) + sizeof(rgb);
    }


    //apply memory for bmp data
    unsigned char *bmp = calloc(img_height, row_size);
    if (bmp == NULL) {
        printf("Failed to apply memory for bmp data\n");
        exit(0);
    }
    printf("Memory applied for bmp data\n");

    for (int i = 0; i < img_height; ++i) {
        for (int j = 0; j < img_width; ++j) {
            bmp[i * row_size + j] = raw[(img_height - 1 - i) * img_width + j];
        }
    }

    //write bmp file
    FILE *bmp_fp = fopen(bmp_path, "wb");
    if (raw_fp == NULL) {
        printf("Failed to open bmp file\n");
        exit(0);
    } else printf("Bmp file opened\n");

    fwrite(&bmp_fh, sizeof(BITMAPFILEHEADER), 1, bmp_fp); //write bmp file header
    fwrite(&bmp_ih, sizeof(BITMAPINFOHEADER), 1, bmp_fp); //write bmp info header
    fwrite(&rgb, sizeof(RGBQUAD), gray_level, bmp_fp); //write palette
    fwrite(bmp, img_height, row_size, bmp_fp); //write image data
    fclose(bmp_fp);
    printf("Bmp file closed\n");
    free(bmp);

    //set counter to 0
    memset(counter, 0, gray_level * sizeof(uint32_t));
    //count histogram
    for (int i = 0; i < img_height; ++i) {
        for (int j = 0; j < img_width; ++j) {
            intensity = *(raw + j + i * img_width);
            counter[intensity]++;
        }
    }
    free(raw);
    printf("====== Histogram ======\n"
           "Intensity   |      Times\n"
           "––––––––––––––––––––––––\n");

    for (int i = 0; i < 256; ++i) {
        printf("%-12d|", i);
        for (int j = 0; j < counter[i] / 50; ++j) printf("-");
        printf("%d\n", counter[i]);
    }
    return 114514;
}

