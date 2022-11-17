class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):

        area1=(ax2-ax1)*(ay2-ay1)
        area2=(bx2-bx1)*(by2-by1)
        double=0
        length=0
        width=0

        if ax2<bx1 or bx2<ax1:
            length=0
        else:
            xs=[ax1,bx1,bx2,ax2]
            xs.sort()
            length=xs[2]-xs[1]
        
        if ay2<by1 or by2<ay1:
            width=0
        else:
            ys=[ay1,by1,by2,ay2]
            ys.sort()
            width=ys[2]-ys[1]

        double=width*length

        total=area1+area2-double
        return total