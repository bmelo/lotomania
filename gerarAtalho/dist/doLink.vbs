Set oWS = WScript.CreateObject("WScript.Shell")
sLinkFile = "D:\Documents and Settings\All Users\Desktop\LotoMania.LNK"
Set oLink = oWS.CreateShortcut(sLinkFile)

oLink.TargetPath = "C:\Documents and Settings\Bruno\Meus documentos\Documentos\Trabalhos\Loteria\FINAL\gerarAtalho\dist\loteria.exe"
   '	oLink.Arguments = ""
oLink.Description = "Programa para LotoMania"
   '	oLink.HotKey = ""
   '	oLink.IconLocation = "C:\Documents and Settings\Bruno\Meus documentos\Documentos\Trabalhos\Loteria\FINAL\gerarAtalho\dist\loteria.exe, 2"
   '	oLink.WindowStyle = "1"
oLink.WorkingDirectory = "C:\Documents and Settings\Bruno\Meus documentos\Documentos\Trabalhos\Loteria\FINAL\gerarAtalho\dist"
oLink.Save