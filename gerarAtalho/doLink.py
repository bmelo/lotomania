import os

nomeArq = "doLink.vbs"
dirAtual = os.getcwd()

os.system("echo %allusersprofile% > todos.fld")
arq = open("todos.fld","r")
dirTodos = str(arq.read()).strip("\n ")
arq.close()

arq = open(nomeArq,"w")

texto = 'Set oWS = WScript.CreateObject("WScript.Shell")\n'
texto+= 'sLinkFile = "'+dirTodos+'\Desktop\LotoMania.LNK"\n'
texto+= 'Set oLink = oWS.CreateShortcut(sLinkFile)\n\n'

texto+= 'oLink.TargetPath = "'+dirAtual+'\loteria.exe"\n'
texto+= '   \'	oLink.Arguments = ""\n'
texto+= 'oLink.Description = "Programa para LotoMania"\n'
texto+= '   \'	oLink.HotKey = ""\n'
texto+= '   \'	oLink.IconLocation = "'+dirAtual+'\loteria.exe, 2"\n'
texto+= '   \'	oLink.WindowStyle = "1"\n'
texto+= 'oLink.WorkingDirectory = "'+dirAtual+'"\n'
texto+= 'oLink.Save'

arq.writelines(texto)
arq.close()

comando = "CSCRIPT "+nomeArq
os.system(comando)

#os.system("echo %allusersprofile%")
#process = subprocess.Popen(['cmd', 'echo %allusersprofile%'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
#print process.communicate()
