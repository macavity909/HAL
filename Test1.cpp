/*
 * TestApplication1.cpp
 *
 * Created: 5/13/2017 1:29:03 PM
 *  Author: PEPINKO
 */ 


#include <avr/io.h>
#define F_CPU 12000000UL
#include <util/delay.h>
#include "mylib.h"
 
#include<stdint.h>
#include<stdlib.h>  

int main(void)
{
initUSART();
initADC();
TCCR1B |= (1<<CS12) | (1<<CS10); 
uint16_t adcValue;
uint16_t timerValue = 0; 
uint8_t isD_Set = false;
uint8_t isL_Set = false;
//uint16_t d = 1;
//uint8_t cnt = 0;
while(1)
{
/*
print_Digit16(cnt);
print_String("\n");
cnt=cnt + d;
if(cnt>60) d = -1;
if(cnt<1) d = 1;
_delay_ms(250);
    */
adcValue = readADC();
 
if(adcValue<250)
{
if(isD_Set == false && isL_Set == false)
{
TCNT1 = 0;
isD_Set = true; 
}
if(isD_Set == false && isL_Set == true)
{
TCNT1 = 0;
isD_Set = true;
}
if(isD_Set == true && isL_Set == true)
{
//TCNT1 = 0;
if(timerValue>0) 
{ 
timerValue = timerValue + TCNT1;
print_Digit16(timerValue);
print_String(" \n ");
timerValue = 0;
}
timerValue = TCNT1;
isD_Set = false;
isL_Set = false;
//print_String(" - ");
//print_Digit16(adcValue);
//transmit_byte(0x20);
}
}
 
if(adcValue >750)
{
isL_Set = true;
} 
//print_String(" - ");print_Digit16(adcValue);print_String(" - ");
//_delay_ms(500);
 
}
}