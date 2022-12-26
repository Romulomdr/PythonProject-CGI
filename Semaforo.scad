$fn= 200;
ligarDesligar = true;

//module abaixo cria um semaforo
module semafaroEstrada(){
    
    rotate([90,0,0]);
    color("grey",1.0) cylinder(15,1,1);
    color("grey",1.0) translate([0,0,15]) sphere(1);
    color("grey",1.0) translate([0,0,15]) rotate([90,0,0]) cylinder(8,1,1);
    color("grey",1.0) translate([-1,-10,11.3]) cube([2,4,7]);
    translate([-0.5,-8,17]) sphere(1);
    color("yellow",1.0) translate([-0.5,-8,14.8]) sphere(1);
    color("red",1.0) translate([-0.5,-8,17]) sphere(1);
    color("green",1.0) translate([-0.5,-8,12.6]) sphere(1);
    color("#778899") translate([-100,1,0]) rotate([90,90,0]) cube([1,200,20]);
    for (i=[0:19])
       translate([i*10-100,-8,0.1]) rotate([90,90,0])
         cube([1,4,1.5]);
    }
    //module abaixo cria o tunel
module tunel(){
    difference(){
        color("#8B4513",1.0) translate([10,-19,-1]) cube([90,20,20]);
        color("#8B4513",1.0) rotate([0,90,0]) translate([-4,-9,0]) cylinder(150,9,8);
        intersection();
    }
    
    }
    //module abaixo cria o carro
module carro(){
    tamanhoTriangulo1 = 5;
    tamanhoTriangulo2 = 10;
    profundidade = 5;
    //module para criar um triangulo
    module triangle(o_len, a_len, depth, center=false)
{
    centroid = center ? [-a_len/3, -o_len/3, -depth/2] : [0, 0, 0];
    translate(centroid) linear_extrude(height=depth)
    {
        polygon(points=[[0,0],[a_len,0],[0,o_len]], paths=[[0,1,2]]);
    }
}
    //module para criar a cabine do carro fazendo interseção com triangulo
    module cabineCarro(){
    intersection(){
        translate([-25,-15,1]) cube([12,5,7]);
        translate([-20,-10,5]) rotate([90,0,0]) triangle(tamanhoTriangulo1,tamanhoTriangulo2,profundidade);
            }
        }
    color("#FF6347") translate([14,3.7,-8]) scale([2,1.3,2]) cabineCarro();
    color("white",1.0) translate([-22.5,-15,2]) sphere(2);
    color("white",1.0) translate([-15.5,-15,2]) sphere(2);
    color("white",1.0) translate([-15.5,-10,2]) sphere(2);
    color("white",1.0) translate([-22.5,-10,2]) sphere(2);

}

semafaroEstrada();
tunel();
carro();
