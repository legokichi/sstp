
use Socket;

$script='Hello World!';
$sender='カードキャプター';

$port=9821;
$addr=$ENV{'HTTP_X_FORWARDED_FOR'};
if (index($addr,'.')==-1) { $addr = $ENV{'REMOTE_ADDR'}; }

$proto = getprotobyname('tcp');
socket(S, PF_INET, SOCK_STREAM, $proto);
$ent = sockaddr_in($port, inet_aton($addr));
connect(S, $ent) || die;
select(S); $| = 1; select(STDOUT);

print S "COMMUNICATE SSTP/1.1\r\n";
print S "Sender: カードキャプター\r\n";
print S "Sentence: 今日は寒いなー。\r\n";
print S "Option: substitute\r\n";
print S "Charset: Shift_JIS\r\n";
print S "\r\n";

$result = <S>;
while (<S>) { print; }
close(S);

return($result);

