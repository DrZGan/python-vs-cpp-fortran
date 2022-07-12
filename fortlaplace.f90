program main
implicit none

integer npoints,i,j,k,nsize
parameter(npoints = 1000, nsize = 1020)
real u_xy(nsize,nsize), added(nsize,nsize)
real :: start, finish
do i=1,npoints
do j=1,npoints
	u_xy(i,j)=0.0
    added(i,j)=1.0
enddo
enddo

call cpu_time(start)
do k=1,2000
    do i=2,npoints-1
    do j=2,npoints-1
	    u_xy(i,j)=u_xy(i,j)*0.1 + added(i,j)
    enddo
    enddo
enddo
call cpu_time(finish)
print '("Time = ",f6.3," seconds.")',finish-start

stop
end