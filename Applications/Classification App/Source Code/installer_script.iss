[Setup]
AppName=SAVE Classification App
AppVersion=1.0
DefaultDirName={pf}\SAVE Classification App
DefaultGroupName=SAVE Classification App
OutputBaseFilename=SAVE_Classification_App_Installer
Compression=lzma
SolidCompression=yes
DisableDirPage=yes
DisableProgramGroupPage=yes
[Files]
Source: "C:\Users\karma\Downloads\Classification App\Source Code\dist\App\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SAVE Classification App"; Filename: "{app}\App.exe"; IconFilename: "{app}\icon.ico"
Name: "{group}\Uninstall SAVE Classification App"; Filename: "{uninstallexe}"
Name: "{commondesktop}\SAVE Classification App"; Filename: "{app}\App.exe"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"; Flags: checkedonce


