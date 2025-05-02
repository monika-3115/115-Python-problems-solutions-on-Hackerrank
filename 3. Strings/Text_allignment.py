# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
[print(("H"*i).rjust(n-1) + "H" + ("H"*i).ljust(n-1)) for i in range(n)]
[print(("H"*n).rjust(n+(n//2)) + ("H"*n).rjust(n*4)) for i in range(n+1)]
[print(("H"*(n*5)).center((n*5)+(n//2)*2)) for i in range((n//2)+1)]
[print(("H"*n).rjust(n+(n//2)) + ("H"*n).rjust(n*4)) for i in range(n+1)]
[print((("H"*i).rjust(n-1) + "H" + ("H"*i).ljust(n-1)).rjust((n*5)+(n//2)*2)) for i in range(n-1, -1, -1)]