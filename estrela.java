void setup() {
    size(400, 400);
}

void criarEstrela(float x, float y, float raioInterno, float raioExterno, int numPontas) {
    float angle = TWO_PI / numPontas;
    float metAng = angle/2.0;
    beginShape();
    for (float a = 0; a < TWO_PI; a += angle) {
        //cada iteracao cria um lado da estrela
        //comecando pelos pontos externos
        float px = x + cos(a) * raioExterno;
        float py = y + sin(a) * raioExterno;
        vertex(px, py);

        //conectando aos pontos internos
        px = x + cos(a+metAng) * raioInterno;
        py = y + sin(a+metAng) * raioInterno;
        vertex(px, py);
    }
    endShape();
}

void draw() 
{
    background(0);//limpar a tela
    translate(width*0.5, height*0.5);//rodar no centro da tela
    rotate(frameCount / 50.0);//mudar o sinal muda o sentido da rotacao
    criarEstrela(0, 0, 30, 70, 5);
}