arq = open("botoes.txt","w");

posL = posT = x = 0
while x<100:
    codigo='<child>\n<widget class="GtkCheckButton" id="ck'+str(x).rjust(2,"0")+'">\n<property name="visible">True</property>\n'
    codigo = codigo + '<property name="can_focus">True</property>\n<property name="label" translatable="yes">'+str(x).rjust(2,"0")+'</property>\n<property name="relief">GTK_RELIEF_HALF</property>\n'
    codigo = codigo + '<property name="response_id">'+str(x)+'</property>\n<property name="draw_indicator">True</property>\n<signal name="clicked" handler="bt_selecao"/>\n</widget>\n'
    if posL>0:
        codigo = codigo + '<packing>\n<property name="left_attach">'+str(posL)+'</property>\n'
        codigo = codigo + '<property name="right_attach">'+str(posL+1)+'</property>\n'
    if posT>0:
        if posL==0:
            codigo = codigo + '<packing>\n'
        codigo = codigo + '<property name="top_attach">'+str(posT)+'</property>\n'
        codigo = codigo + '<property name="bottom_attach">'+str(posT+1)+'</property>\n'
    if posT>0 or posL>0:
        codigo = codigo + '</packing>\n'
    codigo = codigo + '</child>\n'
    arq.writelines(codigo)
    x=x+1
    posL = posL+1
    if posL==10:
        posL=0
        posT = posT+1
    

arq.close()
