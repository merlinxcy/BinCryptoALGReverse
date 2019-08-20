#include<iostream>
#include<string.h>
using namespace std;
unsigned T[65];

void MD5Updata(unsigned &A, unsigned &B, unsigned &C, unsigned &D, char *buffer);

int maidn()
{
	T[1] = 0xd76aa478;         T[17] = 0xf61e2562;            T[33] = 0xfffa3942;         T[49] = 0xf4292244;
	T[2] = 0xe8c7b756;         T[18] = 0xc040b340;            T[34] = 0x8771f681;        T[50] = 0x432aff97;
	T[3] = 0x242070db;         T[19] = 0x265e5a51;            T[35] = 0x6d9d6122;        T[51] = 0xab9423a7;
	T[4] = 0xc1bdceee;         T[20] = 0xe9b6c7aa;            T[36] = 0xfde5380c;        T[52] = 0xfc93a039;
	T[5] = 0xf57c0faf;         T[21] = 0xd62f105d;            T[37] = 0xa4beea44;        T[53] = 0x655b59c3;
	T[6] = 0x4787c62a;         T[22] = 0x02441453;            T[38] = 0x4bdecfa9;        T[54] = 0x8f0ccc92;
	T[7] = 0xa8304613;         T[23] = 0xd8a1e681;            T[39] = 0xf6bb4b60;        T[55] = 0xffeff47d;
	T[8] = 0xfd469501;         T[24] = 0xe7d3fbc8;            T[40] = 0xbebfbc70;        T[56] = 0x85845dd1;
	T[9] = 0x698098d8;         T[25] = 0x21e1cde6;            T[41] = 0x289b7ec6;        T[57] = 0x6fa87e4f;
	T[10] = 0x8b44f7af;         T[26] = 0xc33707d6;            T[42] = 0xeaa127fa;        T[58] = 0xfe2ce6e0;
	T[11] = 0xffff5bb1;         T[27] = 0xf4d50d87;            T[43] = 0xd4ef3085;        T[59] = 0xa3014314;
	T[12] = 0x895cd7be;         T[28] = 0x455a14ed;            T[44] = 0x04881d05;        T[60] = 0x4e0811a1;
	T[13] = 0x6b901122;         T[29] = 0xa9e3e905;            T[45] = 0xd9d4d039;        T[61] = 0xf7537e82;
	T[14] = 0xfd987193;         T[30] = 0xfcefa3f8;            T[46] = 0xe6db99e5;        T[62] = 0xbd3af235;
	T[15] = 0xa679438e;         T[31] = 0x676f02d9;            T[47] = 0x1fa27cf8;        T[63] = 0x2ad7d2bb;
	T[16] = 0x49b40821;         T[32] = 0x8d2a4c8a;            T[48] = 0xc4ac5665;        T[64] = 0xeb86d391;
	unsigned A = 0x67452301, B = 0xEFCDAB89, C = 0x98BADCFE, D = 0x10325476;
	unsigned E = 0xC3D2E1F0;
	char buffer[64] = { '\0' };
	char t_Name[64], t_Code[64], Name[64] = "DiKeN", Code[64] = "0";
	unsigned len_tName, len_tCode, len_Name, len_Code;
	long len_byte_Name;
	cout << "Name:";
	cin >> t_Name;
	len_tName = strlen(t_Name);
	strcat(Name, t_Name);
	if (Name[0] == '\0' || len_tName>0x1E) {
		printf("%x,%x\n", (unsigned)Name[0], len_tName);
		cout << "Error!" << endl;
		return 1;
	}

	len_Name = strlen(Name); len_Code = strlen(Code);
	//消息填充 
	memcpy(&buffer, &Name, len_Name);
	buffer[len_Name] = '\x80';
	len_byte_Name = len_Name << 3;//计算bit数 
	if (len_byte_Name>0xFF) {
		buffer[56] = (char)(len_byte_Name & 0x000000FF);
		buffer[57] = (char)(len_byte_Name & 0x0000FF00);
	}
	else
		buffer[56] = (char)len_byte_Name;
	MD5Updata(A, B, C, D, buffer);
	A = A + 0x67452301;
	B = B + 0xEFCDAB89;
	C = C + 0x98BADCFE;
	D = D + 0x10325476;
	A = A^B^C^D^E;
	printf("Code:%u", (unsigned)A);
	return 0;
}

unsigned md5_ROL(unsigned m, unsigned A, int size) {
	return A + ((m >> (32 - size)) | (m << size));
}
void MD5Updata(unsigned &A, unsigned &B, unsigned &C, unsigned &D, char *buffer) {
	unsigned c[64];
	c[0] = c[4] = c[8] = c[12] = 0x7;
	c[1] = c[5] = c[9] = c[13] = 0xC;
	c[2] = c[6] = c[10] = c[14] = 0x11;
	c[3] = c[7] = c[11] = c[15] = 0x16;
	c[16] = c[20] = c[24] = c[28] = 0x5;
	c[17] = c[21] = c[25] = c[29] = 0x9;
	c[18] = c[22] = c[26] = c[30] = 0xe;
	c[19] = c[23] = c[27] = c[31] = 0x14;
	c[32] = c[36] = c[40] = c[44] = 0x4;
	c[33] = c[37] = c[41] = c[45] = 0xb;
	c[34] = c[38] = c[42] = c[46] = 0x10;
	c[35] = c[39] = c[43] = c[47] = 0x17;
	c[48] = c[52] = c[56] = c[60] = 0x6;
	c[49] = c[53] = c[57] = c[61] = 0xa;
	c[50] = c[54] = c[58] = c[62] = 0xf;
	c[51] = c[55] = c[59] = c[63] = 0x15;

	//FF();
	int i, j;
	i = 0; j = 0;
	for (; i<16; i++)
	{
		j = 4 * i;
		unsigned m_a = ((unsigned)buffer[j] & 0x000000FF) + ((unsigned)buffer[j + 1] * 0x100 & 0x0000FF00) + ((unsigned)buffer[j + 2] * 0x10000 & 0x00FF0000) + ((unsigned)buffer[j + 3] * 0x1000000 & 0xFF000000);
		if (i % 4 == 0)
		{
			A = md5_ROL(A + m_a + T[i + 1] + ((C^D)&B^D), B, c);
		}

		else if (i % 4 == 1)
		{
			D = md5_ROL(D + m_a + T[i + 1] + ((B^C)&A^C), A, c);
		}
		else if (i % 4 == 2)
		{
			C = md5_ROL(C + m_a + T[i + 1] + ((A^B)&D^B), D, c);
		}
		else
		{
			B = md5_ROL(B + m_a + T[i + 1] + ((D^A)&C^A), C, c);
		}

	}
	//GG()
	i = 0; j = 0;
	for (; i<16; i++)
	{
		j = 4 * (((5 * i) + 1) % 16);
		unsigned m_a = ((unsigned)buffer[j] & 0x000000FF) + ((unsigned)buffer[j + 1] * 0x100 & 0x0000FF00) + ((unsigned)buffer[j + 2] * 0x10000 & 0x00FF0000) + ((unsigned)buffer[j + 3] * 0x1000000 & 0xFF000000);

		if (i % 4 == 0)
		{
			A = md5_ROL(A + m_a + T[i + 17] + ((C^B)&D^C), B, c[i + 16]);
		}

		else if (i % 4 == 1)
		{
			D = md5_ROL(D + m_a + T[i + 17] + ((B^A)&C^B), A, c[i + 16]);
		}
		else if (i % 4 == 2)
		{
			C = md5_ROL(C + m_a + T[i + 17] + ((A^D)&B^A), D, c[i + 16]);
		}
		else
		{
			B = md5_ROL(B + m_a + T[i + 17] + ((D^C)&A^D), C, c[i + 16]);
		}
	}

	//HH()
	i = 0; j = 0;
	for (; i<16; i++)
	{
		j = 4 * ((3 * i + 5) % 16);
		unsigned m_a = ((unsigned)buffer[j] & 0x000000FF) + ((unsigned)buffer[j + 1] * 0x100 & 0x0000FF00) + ((unsigned)buffer[j + 2] * 0x10000 & 0x00FF0000) + ((unsigned)buffer[j + 3] * 0x1000000 & 0xFF000000);

		if (i % 4 == 0)
		{
			A = md5_ROL(A + m_a + T[i + 33] + (C^B^D), B, c[i + 32]);
		}

		else if (i % 4 == 1)
		{
			D = md5_ROL(D + m_a + T[i + 33] + (B^A^C), A, c[i + 32]);
		}
		else if (i % 4 == 2)
		{
			C = md5_ROL(C + m_a + T[i + 33] + (A^D^B), D, c[i + 32]);
		}
		else
		{
			B = md5_ROL(B + m_a + T[i + 33] + (D^C^A), C, c[i + 32]);
		}
	}

	//II()
	i = 0; j = 0;
	for (; i<16; i++)
	{
		j = 4 * ((7 * i) % 16);
		unsigned m_a = ((unsigned)buffer[j] & 0x000000FF) + ((unsigned)buffer[j + 1] * 0x100 & 0x0000FF00) + ((unsigned)buffer[j + 2] * 0x10000 & 0x00FF0000) + ((unsigned)buffer[j + 3] * 0x1000000 & 0xFF000000);
		if (i % 4 == 0)
		{
			A = md5_ROL(A + m_a + T[i + 49] + (((~D) | B) ^ C), B, c[i + 48]);
		}
		else if (i % 4 == 1)
		{
			D = md5_ROL(D + m_a + T[i + 49] + (((~C) | A) ^ B), A, c[i + 48]);
		}
		else if (i % 4 == 2)
		{
			C = md5_ROL(C + m_a + T[i + 49] + (((~B) | D) ^ A), D, c[i + 48]);
		}
		else
		{
			B = md5_ROL(B + m_a + T[i + 49] + (((~A) | C) ^ D), C, c[i + 48]);
		}
	}
}
