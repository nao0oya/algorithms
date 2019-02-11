"""
時計
秒単位の時間 Sが与えられるので、h:m:sの形式へ変換して出力してください。ここで、
hは時間、
mは 60 未満の分、
sは 60 未満の秒とします。

Input
Sが１行に与えられます。

Output
h、m、sを :（コロン）区切りで１行に出力してください。数値が１桁の場合、0 を付けて２桁表示をする必要はありません。

Constraints
0≤S<86400
Sample Input
46979
Sample Output
13:2:59
"""

x = int(input())
h, mod = divmod(x, 3600)
m, s = divmod(mod, 60)

print('%d:%d:%d' % (h, m, s))