# CUI 필수 명렁어 정리  

### [Manual](https://youtu.be/EL6AQl-e3AQ?t=274) (사용자 메뉴얼) 

```bash 
~$ man        # Get-Help
~$ man clear  # clear 명령어의 메뉴얼을 보여줌 
```



### [Nvigating file system](https://youtu.be/EL6AQl-e3AQ?t=351) (파일 시스템 탐색하기)

```bash 
~$ pwd       # print working directory 
~$ man pwd   # pwd 명령어가 뭔지 설명서 메뉴얼 나옴 
```

```bash
~$ ls     # list in the path 

~$ ls <지정 경로>    # 특정 경로의 리스트 
~$ ls -l    # list long  (세부 정보 표시)
~$ ls -a    # list all  (숨김 파일 확인)
~$ ls -al   # ll 명령어랑 동일 
```

```bash 
~$ open .       # 현재 경로를 GUI 파일 탐색기로 열기 (Mac 용)
~$ xdg-open .   # (ubuntu 용)
```

```bash
~$ cd <경로>      # change directory (현재 경로에서 어디로 이동할래?)
~$ cd .          # 현재 경로로 이동 ㅎ 
~$ cd ..         # 현재 경로의 상위 경로로 이동 
~$ cd ~          # $HOME 으로 이동 
~$ cd -          # 현재 경로로 이동하기 직전의 경로로 이동 (매우 유용! ㅇ_ ㅇ!)
```

```bash
~$ find . -type f -name "*.txt"   # 현재 경로(.) 부터 시작해서 
								  # 데이터 타입은 file 인데 
								  # 이름은 .txt로 끝나는 데이터를 찾아라 
								  
~$ find . -type d -name "*2"   # 현재 경로(.) 부터 시작해서 
							   # 데이터 타입은 directory 인데 
							   # 이름은 '2' 로 끝나는 데이터를 찾아라 								  
```

```bash 
~$ which        # 내가 실행하려는 프로그램이 어디에 설정되어 있는지 경로 확인 
				# 즉, 특정 명령어의 위치를 찾아줌 
				
~$ which find   # find 라는 명령어가 어느 경로에 설정돼 있는지 찾아줌 		

```



### [Create and manage files](https://youtu.be/EL6AQl-e3AQ) (파일 생성 및 관리하기)

```bash
~$ touch test.txt    # test.txt 라는 file 이 없다면 생성 
					 # 이미 있다면 해당 파일의 수정 날짜를 touch 한 시점으로 업데이트 			 
```

```bash 
~$ cat test.txt      # concatenate and print files 
					 # text.txt 파일의 내용물을 프린트 

~$ cat text1.txt text2.txt   # text1.txt 와 text2.txt의 내용을 연결시켜서 프린트 
```

 ```bash 
 ~$ echo <문자열> 				 # 문자열을 터미널에 메아리 처럼 에코 
 ~$ echo "hello world"  
 
 
 # Echo 활용 
 ~$ echo "hello world" > new_file.txt  # "hello world" 문자열을 
 									  # new_file.txt 덮어써서 입력 (기존 내용 지워짐)
 
 ~$ echo "hello world" >> new_file.txt # 기존 내용 밑에다가 덧붙임 (extend)
 ```

```bash 
~$ mkdir <디렉토리 이름>    # make directory 


~$ mkdir -p dir4/subdir1/subdir2   # subdir2 디렉토리를 생성하는데 
								  # 중간중간 해당 부모경로(parents)에 해당 디렉토리가 없으면 
								  # 자동으로 만들어서 subdir2 생성						  
```



```bash 
~$ cp file1.txt ./dir1      # copy 
							# file1.txt 파일을 
							# ./dir1 로 복사 (ctrl + c  & ctrl + v)

~$ mv file1.txt ./dir1      # move 
							# file1.txt 파일을 
							# ./dir1 로 이동 (ctrl + x & ctrl + v)

~$ mv file1.txt file2.txt   # file1.txt 파일을 file2.txt 파일로 이동 
							# 즉, 이름 바꾸기 
```

```bash 
~$ rm file1.txt  # remove 
				 # file1.txt 파일 삭제 
                                
~$ rm -rf ./dir2  # recursive & force (재귀적이고 강제적으로)            
				  # ./dir2 디렉토리 하위 경로를 포함해서 삭제 
```

```bash 
~$ grep        # global regular expression print 
```













***

### Reference 

[1] [필수 리눅스 터미널 명렁어 정리 | 배쉬, 파워쉘 (Bash, PowerShell)튜토리얼! 가좌아, youtube](https://youtu.be/EL6AQl-e3AQ) / 