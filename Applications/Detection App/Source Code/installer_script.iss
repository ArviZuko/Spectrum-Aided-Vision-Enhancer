[Setup]
AppName=SAVE Detection App
AppVersion=1.0
DefaultDirName={pf}\SAVE Detection App
DefaultGroupName=SAVE Detection App
OutputBaseFilename=SAVE_Detection_App_Installer
Compression=lzma
SolidCompression=yes
DisableDirPage=yes
DisableProgramGroupPage=yes
[Files]
Source: "C:\Users\karma\Downloads\Detection App\Source Code\dist\App\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SAVE Detection App"; Filename: "{app}\App.exe"; IconFilename: "{app}\icon.ico"
Name: "{group}\Uninstall SAVE Detection App"; Filename: "{uninstallexe}"
Name: "{commondesktop}\SAVE Detection App"; Filename: "{app}\App.exe"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: checkedonce


