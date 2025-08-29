If you made it so far,<br/> 
Congratulations — I will now<br/>
lower the bar.<br/>
<br/>
The image tags might show<br/>
some information you maybe didn’t know.<br/>
You knew? Okay, then no...<br/>
(Sad noises)<br/>
<br/>
Go further — the choice is yours.<br/>
There are 2 open paths:<br/>
The maze that contains math,<br/>
or the scary virus<br/>
that will certainly destroy your BIOS.<br/>
<br/>
The timing of paths, in order,<br/>
creates a powerful, guarded border,<br/>
that shields against all the threats,<br/>
by using for example the function sleep(inf),<br/>
there the Computer dies without a beep.<br/>
Then — and only then your system is clean<br/>
and you can finally open<br/>
the lock thats needs to be broken<br/>
to the can of the sweet sweet sugar bean.<br/>

<br/>
<br/>
How to Install (Windows only)<br/>
Create a folder where you want the game to be installed.<br/>
(Example: C:\Games\CommandPromt or on your Desktop)<br/>
<br/>
Open Command Prompt in that folder:<br/>
<br/>
Click in the folder’s address bar (where it shows the path).<br/>
<br/>
Type cmd and press Enter.<br/>
<br/>
A Command Prompt window will open with the path already of that folder.<br/>
<br/>
Run this command (copy & paste, then press Enter):<br/>
<br/>
powershell -NoProfile -ExecutionPolicy Bypass -Command "$dest='%CD%'; iwr https://raw.githubusercontent.com/FunPhantasie/Loki/main/install.ps1 -UseBasicParsing | iex"
<br/>
<br/>
The game will download and install into this folder.<br/>
Can take a bit longer than expected.<br/>
<br/>
Bug Fixes:<br/>
IF Not OK:<br/>
<br/>
powershell -NoProfile -Command "try { [Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; [void](Invoke-WebRequest 'https://tls-v1-2.badssl.com/' -Method Head -TimeoutSec 10); 'OK: TLS 1.2 funktioniert.' } catch { 'FEHLER: TLS 1.2 geht nicht: ' + $_.Exception.Message }"
<br/>
Try This:
<br/>
powershell -NoProfile -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]::Tls12; $dest='%CD%'; iwr 'https://raw.githubusercontent.com/FunPhantasie/Loki/main/install.ps1' -UseBasicParsing -Headers @{ 'User-Agent'='WindowsPowerShell/5.1' } | iex"
<br/>
When Geht nicht.
<br/>
powershell -NoProfile -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol=[Net.SecurityProtocolType]3072; $dest='%CD%'; iwr 'https://raw.githubusercontent.com/FunPhantasie/Loki/main/install.ps1' -UseBasicParsing -Headers @{ 'User-Agent'='WindowsPowerShell/5.1' } | iex"
<br/>
 

