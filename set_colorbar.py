fig,ax = plt.subplots(figsize=[11.5,11.5],subplot_kw={'projection': ccrs.PlateCarree()},constrained_layout=True)
img = ax.pcolormesh(gpm_lon,gpm_lat,gpm_rain_int,cmap=plt.get_cmap('Accent', 4),vmin=0,vmax=3) # set how may colors to use
#ax.set_aspect(300)
ax.set_xlim(lon)
ax.set_ylim(lat)
gl=ax.gridlines(draw_labels=True,linestyle='None')
gl.xlabels_top=False
gl.ylabels_right=False
gl.xlines=False
gl.ylines=False
gl.xlabel_style={'size':fontsz,'color':'black'}
gl.ylabel_style={'size':fontsz,'color':'black'}
cb=plt.colorbar(img,shrink=0.35,pad=0.04) #set colorbar
cb.ax.tick_params(labelsize=fontsz)
cb.set_label(label='Rain Type',size=fontsz)
cb.set_ticks([0,1,2,3])
cb.ax.set_yticklabels(['No Rain','Stratiform','Convection','Other'])
p1=plt.scatter(OTlon,OTlat,s=20,c=OTprob,cmap=plt.get_cmap('bwr'),vmin=0,vmax=1)
