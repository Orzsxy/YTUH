#include <stdio.h> 
#include <string.h> 
float get_cpu_clock_speed () 
{ 
      FILE* fp; 
      char buffer[1024]; 
      size_t bytes_read; 
      char* match; 
      float clock_speed; 
       
      fp = fopen ("/proc/cpuinfo", "r"); //已只读的方式打开/proc/cpuinfo
      bytes_read = fread (buffer, 1, sizeof (buffer), fp); //将文件流fp中1个buffer大小的数据存入数组buffer中，并将读取到得对象个数赋给bytes_read
      fclose (fp);   
      if (bytes_read == 0 || bytes_read == sizeof (buffer)) //如果读取的对象个数为0，则返回0；如果读取对象个数为sizeof（buffer）也返回0，因为下一条语句要将buffer[]的最后一个非空位置置为'\0'。
      	return 0; 
      buffer[bytes_read] = '\0'; 
      match = strstr (buffer, "cpu MHz");			//匹配   将buffer中cpu MHz的地址赋给match。
      if (match == NULL) 
      	return 0; 
      sscanf (match, "cpu MHz : %f", &clock_speed);	//读取 	 我的理解为在/proc/cpuinfo中，CPU的频率就存储在文件中cpu MHz的位置，所以此处将CPU的频率赋给&clock_speed
      return clock_speed; 
} 
int main (void) 
{ 
      printf ("CPU clock speed: %4.0f MHz\n", get_cpu_clock_speed ()); 
      return 0; 
}
