#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void xor_encrypt_decrypt(const char *input_path, const char *output_path, const char *key) {
    FILE *input = fopen(input_path, "rb");
    FILE *output = fopen(output_path, "wb");

    if (!input || !output) {
        perror("Error opening files");
        exit(1);
    }

    size_t key_len = strlen(key);
    size_t i = 0;
    int ch;

    while ((ch = fgetc(input)) != EOF) {
        fputc(ch ^ key[i % key_len], output);
        i++;
    }

    fclose(input);
    fclose(output);

    printf("Operation completed: %s -> %s\n", input_path, output_path);
}

int main(int argc, char *argv[]) {
    if (argc != 5) {
        printf("Usage: %s <encrypt|decrypt> <input file> <output file> <key>\n", argv[0]);
        return 1;
    }

    const char *mode = argv[1];
    const char *input_file = argv[2];
    const char *output_file = argv[3];
    const char *key = argv[4];

    if (strcmp(mode, "encrypt") == 0 || strcmp(mode, "decrypt") == 0) {
        xor_encrypt_decrypt(input_file, output_file, key);
    } else {
        printf("Invalid mode. Use 'encrypt' or 'decrypt'.\n");
        return 1;
    }

    return 0;
}
