// https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d8565

#include <bits/stdc++.h>
#include <stdio.h>
#include <math.h>
using namespace std;

int T, i=1;
double amount;
double logs[200001];
int W, H, L, U, R, D;
int w, h, r, d;

int main(){
    logs[0] = 0;
    for(int x=1; x<200001; x++)
        logs[x] = logs[x-1] + log2(x);
    cin >> T;
    while(T--){
        cin >> W >> H >> L >> U >> R >> D;
        if((L==1 && U==1) || (D-U+1==H) || (R-L+1==W)){
            cout << "Case #" << i++ << ": 0.0" << endl;
            continue;
        }
        amount = 0.0;
        if(1<L && D<H){
            d = D;
            w = L-2;
            while(w >= 0){
                amount += pow(2.0,(logs[d+w] - logs[d] - logs[w] - d - w));
                d++;
                w--;
            }
        }
        if(1<U && R<W){
            r = R;
            h = U-2;
            while(h >= 0){
                amount += pow(2.0, (logs[r+h] - logs[r] - logs[h] - r - h));
                r++;
                h--;
            }
        }
        cout << "Case #" << i++ << ": " << amount << endl;
    }
    return 0;
}
