nsize=(6,3.5)
plt.figure(figsize=winsize)
img=plt.pcolormesh(mod_lon,mod_lat,data,cmap='gray',vmin=0,vmax=1)
plt.xlim(lon)
plt.ylim(lat)
#gl=plt.gridlines(draw_labels=True,linestyle='None')
#gl.xlabels_top=False
#gl.ylabels_right=False
#gl.xlines=False
#gl.ylines=False
#gl.xlabel_style={'size':fontsz,'color':'black'}
#gl.ylabel_style={'size':fontsz,'color':'black'}
plt.rcParams['font.size'] = '15'
cb=plt.colorbar(img,ticks=cbtick)#shrink=shrink,pad=pad 
cb.ax.tick_params(labelsize=fontsz)
cb.set_label(label='Reflectance 0.65 $\mu$m',size=fontsz)

p1=plt.scatter(OTlon,OTlat,s=20,c=OTprob,cmap=plt.get_cmap('bwr'),vmin=0,vmax=1)
cb1=plt.colorbar(p1,ticks=ptick)#shrink=shrink,pad=pad, 
cb1.ax.tick_params(labelsize=fontsz)
cb1.set_label(label='OT Probability',size=fontsz)
