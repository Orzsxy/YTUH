#include <stdio.h> 
#include <string.h> 
float get_cpu_clock_speed () 
{ 
      FILE* fp; 
      char buffer[1024]; 
      size_t bytes_read; 
      char* match; 
      float clock_speed; 
       
      fp = fopen ("/proc/cpuinfo", "r"); //��ֻ���ķ�ʽ��/proc/cpuinfo
      bytes_read = fread (buffer, 1, sizeof (buffer), fp); //���ļ���fp��1��buffer��С�����ݴ�������buffer�У�������ȡ���ö����������bytes_read
      fclose (fp);   
      if (bytes_read == 0 || bytes_read == sizeof (buffer)) //�����ȡ�Ķ������Ϊ0���򷵻�0�������ȡ�������Ϊsizeof��buffer��Ҳ����0����Ϊ��һ�����Ҫ��buffer[]�����һ���ǿ�λ����Ϊ'\0'��
      	return 0; 
      buffer[bytes_read] = '\0'; 
      match = strstr (buffer, "cpu MHz");			//ƥ��   ��buffer��cpu MHz�ĵ�ַ����match��
      if (match == NULL) 
      	return 0; 
      sscanf (match, "cpu MHz : %f", &clock_speed);	//��ȡ 	 �ҵ����Ϊ��/proc/cpuinfo�У�CPU��Ƶ�ʾʹ洢���ļ���cpu MHz��λ�ã����Դ˴���CPU��Ƶ�ʸ���&clock_speed
      return clock_speed; 
} 
int main (void) 
{ 
      printf ("CPU clock speed: %4.0f MHz\n", get_cpu_clock_speed ()); 
      return 0; 
}
