;UID:U202112205:  
;Flag:02c1b4:
;Name:������  
;Date:2023��3��15��  
;FileName:mype1.asm
;Other comments�� 
.386
.model flat,stdcall
option casemap:none
include \masm32\include\windows.inc
include \masm32\include\kernel32.inc
includelib \masm32\lib\kernel32.lib
include \masm32\include\user32.inc
includelib \masm32\lib\user32.lib
.data
MsgBox1 db "ID:U202112205;Name:������:PEHost:MessageBox1",0
MsgBox2 db "ID:U202112205;Name:������:PEHost:MessageBox2",0
.code
start:
invoke MessageBox,NULL,addr MsgBox1,addr MsgBox1,MB_OK; �鿴 Using invoke;���õ���API
invoke MessageBox,NULL,addr MsgBox2,addr MsgBox2,MB_OK; ���ý�������API
invoke ExitProcess,0
end start