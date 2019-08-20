#include "stdafx.h"
#include <stdlib.h>
#include <stdio.h>
#include "aes.h"
int main(int argc, char *argv[])
{
	int tmp;
	aes256_context ctx;
	uint8_t key[32];
	memset(key, 0, 32);
	char input_key[] = "m@t1OSXOqIGrb4H!";
	memcpy(key, input_key, sizeof(input_key));
	uint8_t buf[16], i;
	for (i = 0; i < sizeof(buf); i++) buf[i] = i * 16 + i;
	char input_buf[] = "{\"count\":\"3\"}";//16 only
	memset(buf, 16-sizeof(input_buf), 16);
	memcpy(buf, input_buf, sizeof(input_buf));
	//for (i = 0; i < sizeof(key); i++) key[i] = i;
	//DUMP("txt: ", i, buf, sizeof(buf));
	//DUMP("key: ", i, key, sizeof(key));
	printf("---/n");
	aes256_init(&ctx, key);
	aes256_encrypt_ecb(&ctx, buf);
	//DUMP("enc: ", i, buf, sizeof(buf));
	printf("tst: 8e a2 b7 ca 51 67 45 bf ea fc 49 90 4b 49 60 89/n");
	aes256_init(&ctx, key);
	aes256_decrypt_ecb(&ctx, buf);
	//DUMP("dec: ", i, buf, sizeof(buf));
	aes256_done(&ctx);
	return 0;
}