#!/usr/bin/perl
use utf8;
use Socket;

# 通信先IPアドレス取得
$addr = $ENV{'HTTP_X_FORWARDED_FOR'};
if(index($addr, '.') == -1){
	$addr = $ENV{'REMOTE_ADDR'};
}

# タイムアウト処理。
# ベースウェアらの応答が2秒以内に得られないとき。
$SIG{ALRM} = sub {
	close(S);
	print 'Content-type: text/plain'+"\n";
	print "\n";
	print 'SSTP/1.1 408 Request Timeout'+"\r\n";
	print "\r\n";
};

alarm(2);

$ent = sockaddr_in(9801, inet_aton($addr));
socket(S, PF_INET, SOCK_STREAM, getprotobyname('tcp')) || die;
connect(S, $ent) || die;
select(S);
$| = 1;
select(STDOUT);

print S "SEND SSTP/1.1\r\n";
print S "Charset: UTF-8\r\n";
print S "Sender: Legokichi\r\n";
print S "Script: "+'\0Hello \w8World\e'+"\r\n";
print S "\r\n";

alarm(0); 

#レスポンス表示
$result = <S>;
print "Content-type: text/plain\n";
print "\n";
while(<S>){
	print;
}
close(S);
