# two methods to write array to text or write line by line

# write line by line
fname=open('test.txt','w')
fname.write(str(data1)+' '+str(data1)+'\n')
# fname.write('{} {} \n',data1,data2)
fname.close()

# write a whole array
dat=np.array([data1,data2,data3,data4])
dat=dat.T
np.savetxt('atm_file_era.dat',dat,delimiter=' ')
