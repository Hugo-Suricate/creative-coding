class Hex
{
  public int x;
  public int y;
  public int z;
  
  public Hex(int _x, int _y, int _z)
  {
    x =_x; y=_y; z=_z;
  }
  
  public Hex[] neighbours()
  {
    Hex[] n = new Hex[6];
    n[0] = new Hex(x+1, y  , z  );
    n[1] = new Hex(x+1, y+1, z  );
    n[2] = new Hex(x  , y+1, z  );
    n[3] = new Hex(x  , y+1, z+1);
    n[4] = new Hex(x  , y  , z+1);
    n[5] = new Hex(x+1, y  , z+1);
    
    return n;
  }
  
  public Hex[] neighboursRotated()
  {
    Hex[] n = new Hex[6];
    int shift = (6-getQuadrant());
    n[(0+shift)%6] = new Hex(x+1, y  , z  );
    n[(1+shift)%6] = new Hex(x+1, y+1, z  );
    n[(2+shift)%6] = new Hex(x  , y+1, z  );
    n[(3+shift)%6] = new Hex(x  , y+1, z+1);
    n[(4+shift)%6] = new Hex(x  , y  , z+1);
    n[(5+shift)%6] = new Hex(x+1, y  , z+1);
    
    return n;
  }
  
  public int getQuadrant()
  {
    int q = 0;
    if     (x >= y && y >= z)
      return 0;
    else if(y >= x && x >= z)
      return 1;
    else if(y >= z && z >= x)
      return 2;
    else if(z >= y && y >= x)
      return 3;
    else if(z >= x && x >= y)
      return 4;
    else
      return 5;
  }
  
  public void normalize()
  {
    if(x <= y && x <= z)
    {
      y -= x;
      z -= x;
      x = 0;
    }
    else if(y <= x && y <= z)
    {
      x -= y;
      z -= y;
      y = 0;
    }
    else if(z <= x && z <= y)
    {
      x -= z;
      y -= z;
      z = 0;
    }
  }
  
  @Override
  public boolean equals(Object obj)
  {
    if (this == obj)
        return true;
    else if (obj == null)
        return false;
    else if (obj instanceof Hex)
    {
      Hex h = (Hex) obj;
      return (x-y == h.x-h.y) && (y-z == h.y-h.z) && (z-x == h.z-h.x);
    }
    return false;
  }
  
  @Override
  public int hashCode()
  {
    normalize();
    return x + y*256 + z*65536;
  }
}
