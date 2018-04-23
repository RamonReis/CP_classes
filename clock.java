int radius;
ArrayList<Balloon> balloons;
void setup()
{
    s = 400
    background(0);
    size( s, s);
}
void draw(){
    fill(80)
    s = second();
    m = minute();
    
    center= height/2; //square size
    radius = 350;
    mp = radius/4;
    sp = radius/3;
    hp = radius/5;
    
    float rad = PI/4;
    
    sec_ang = map(second(), 0, 60, 0, TWO_PI) - HALF_PI;
    min_ang = map(minute(), 0, 60, 0, TWO_PI) - HALF_PI;
    hour_ang = map( hour() + (minute()  / 60.0), 0, 60, 0, TWO_PI) - HALF_PI ;
    
    print(hour())
    secx = sp * cos(sec_ang);
    secy = sp * sin(sec_ang);
    
    minx = mp * cos(min_ang);
    miny = mp * sin(min_ang);
    
    hourx = hp * cos(hour_ang);
    houry = hp * sin(hour_ang);
    
    //comeco de desenho
    stroke(255, 255, 255);
    
    line(center, 0, center , height);
    line(0, center, height , center);
    ellipse(center, center, radius, radius);
    
    
    stroke(255, 0, 0);
    strokeWeight(4);
    line(center, center, center + hourx, center + houry );//hour
    
    stroke(0, 255, 0);
    strokeWeight(2);
    line(center, center, center + minx, center + miny );//min
    
    stroke(0, 0, 255);
    strokeWeight(1);
    line(center, center, center + secx, center + secy );//sec
    
    fill(180)
    textSize(32);
    text(hour()+":"+minute()+":"+second(), center, center);
    
}