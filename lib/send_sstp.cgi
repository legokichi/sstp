#!/usr/bin/perl
################################################################
# send_sstp Vr.0.01+ Shift_JIS 2001 6/10版(for UNIX)
# タイムアウト実装版
# タイムアウト処理は沢渡 みかげ様より助言頂きました。
# KAIN (http://tech-web.net/)
# 配布元　http://tech-web.net/download/
# 「何か。（仮）」と通信により話させるCGI
# 【構成ファイル】このファイル　画像ファイル　一行ずつの会話
# 【使い方】　<IMG SRC="このCGIのURL">
################################################################
$|=1;
use strict; use Socket; use FileHandle;
my ($con_host, $con_port);
my ($port, $url, $path, $ip, $sockaddr);
my ($arg, $buf, $data);
# ------------------------------------------------------------------
my $port='9801';       # SSTP Port
my $GAZOU='icon.gif';  # Dummy画像を指定
my $KAIWA='kaiwa.txt'; # 会話の入ったファイルを指定(１行１会話)
my $ERROR='error.txt'; # タイムアウトした場合のERRORログ。各自セットして666に。
# ------------------------------------------------------------------
eval {
	local($SIG{ALRM}) = sub {
		close(SOCKET);open(FILE, '>>'.$ERROR);print FILE ${Jdate}."\n";close(FILE);
	};
	alarm(10);
	my $host=$ENV{REMOTE_ADDR} || 'localhost';
	$port||=getservbyname('http', 'tcp');
	$path||= '/'; $con_host = $host; $con_port = $port;
	$ip = inet_aton($con_host) ||  &REDAI;
	$sockaddr = pack_sockaddr_in($con_port, $ip);
	socket(SOCKET, PF_INET, SOCK_STREAM, 0) || &REDAI;
	connect(SOCKET, $sockaddr) || &REDAI;
	SOCKET->autoflush(1);
	open(FILE,$KAIWA); srand; rand($.) < 1 && ($data = $_) while <FILE>; close(FILE);
	print SOCKET "SEND SSTP/1.1\r\nSender: Team TECH-WEB\r\n";
	print SOCKET "Script: \\h\\s[0]$data\\e\r\n";
	# print SOCKET "Script: \\h\\s[0]$data\\u$udata\\e\r\n";
	print SOCKET "Option: nodescript,notranslate\r\n";
	print SOCKET "Charset: Shift_JIS\r\n\r\n\r\n"; # Shift_JISの場合
	# print SOCKET "Charset: EUC-JP\r\n\r\n\r\n"; # EUCの場合
	close(SOCKET); &REDAI;
	alarm(0); 
};
if($@) {
	&REDAI;exit;
}
sub REDAI{
	close(SOCKET);
	print "Cache-Control: no-cache\nPragma: no-cache\nExpires: 0;\nLocation: $GAZOU\n\n";
	exit; 
}
sub Jdate{
		my $times=shift;$times=time unless($times);my ($sec,$min,$hour,$mday,$month,$year,$youbi)=localtime($times);$min = "0$min" if ($min < 10); $month++;$youbi=('日','月','火','水','木','金','土')[$youbi];$year+=1900;my $date="$month/$mday ( $youbi ) $hour 時 $min 分 $sec 秒";return \$date;
	}
exit;
__END__
