/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package imagemcriptografada;

/**
 *
 * @author andy_
 */
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Random;
import javax.imageio.ImageIO;

public class Imagem {

    int[][] matrizImgAlt;
    int[][] matrizOperacao;

    public Imagem() {
    }

    public Imagem(int[][] matrizAlter, int[][] matrizOp) {
        this.matrizImgAlt = matrizAlter;
        this.matrizOperacao = matrizOp;
    }

    public int[][] recebeImagem() throws IOException {
        BufferedImage imagem = ImageIO.read(new File("Monalisa.jpg"));
        int ValoresImagem;
        int MatrizImagem[][] = new int[imagem.getWidth() * 3][imagem.getHeight()];
        for (int itemLarg = 0; itemLarg < imagem.getWidth(); itemLarg++) {
            for (int itemAlt = 0; itemAlt < imagem.getHeight(); itemAlt++) {
                Color c = new Color(imagem.getRGB(itemLarg, itemAlt));
                MatrizImagem[itemLarg * 3][itemAlt] = c.getRed();
                MatrizImagem[itemLarg * 3 + 1][itemAlt] = c.getGreen();
                MatrizImagem[itemLarg * 3 + 2][itemAlt] = c.getBlue();
            }

        }

        return MatrizImagem;
    }

    public Imagem ImagemMultiplicaEscalar(Imagem img, int valor) {
        int matrizResultante[][] = new int[img.matrizImgAlt.length][img.matrizImgAlt[0].length];
        for (int i = 0; i < img.matrizImgAlt.length; i++) {
            for (int j = 0; j < img.matrizImgAlt[0].length; j++) {
                matrizResultante[i][j] = img.matrizImgAlt[i][j] * valor;
            }
        }
        Imagem imagem = new Imagem();
        imagem.matrizImgAlt = matrizResultante;
        return imagem;
    }

    public Imagem ImagemDivideEscalar(Imagem img, int valor) {
        int matrizResultante[][] = new int[img.matrizImgAlt.length][img.matrizImgAlt[0].length];
        for (int i = 0; i < img.matrizImgAlt.length; i++) {
            for (int j = 0; j < img.matrizImgAlt[0].length; j++) {
                matrizResultante[i][j] = img.matrizImgAlt[i][j] / valor;
            }
        }
        Imagem imagem = new Imagem();
        imagem.matrizImgAlt = matrizResultante;
        return imagem;
    }

    public Imagem ImagemSomaMatrizes(int[][] matrizImagem, int limite) {
        int matrizCriptografada[][] = new int[matrizImagem.length][matrizImagem[0].length];
        int matrizOperacao[][] = new int[matrizImagem.length][matrizImagem[0].length];
        Random random = new Random();
        random.nextInt(limite);
        for (int i = 0; i < matrizImagem.length; i++) {
            for (int j = 0; j < matrizImagem[0].length; j++) {
                int valor = random.nextInt(limite);
                if (valor % 2 == 0) {
                    matrizCriptografada[i][j] = matrizImagem[i][j] - valor * valor;
                    matrizOperacao[i][j] = valor;
                } else {
                    matrizCriptografada[i][j] = matrizImagem[i][j] + valor * valor;
                    matrizOperacao[i][j] = valor;
                }

            }
        }

        Imagem imagemCriptografada = new Imagem(matrizCriptografada, matrizOperacao);
        return imagemCriptografada;
    }

    public Imagem ReverteSomaMatrizes(Imagem img) {
        int matrizNormalizada[][] = new int[img.matrizOperacao.length][img.matrizOperacao[0].length];
        for (int i = 0; i < img.matrizImgAlt.length; i++) {
            for (int j = 0; j < img.matrizImgAlt[0].length; j++) {
                int valor = img.matrizOperacao[i][j];
                if (valor % 2 == 0) {
                    matrizNormalizada[i][j] = img.matrizImgAlt[i][j] + valor * valor;
                } else {
                    matrizNormalizada[i][j] = img.matrizImgAlt[i][j] - valor * valor;
                }

            }
        }
        Imagem imagemCriptografada = new Imagem(matrizNormalizada, img.matrizOperacao);
        return imagemCriptografada;

    }

    public Imagem transpor(Imagem img) {
        int matrizResultante[][] = new int[img.matrizImgAlt[0].length][img.matrizImgAlt.length];
        for (int i = 0; i < img.matrizImgAlt[0].length; i++) {
            for (int j = 0; j < img.matrizImgAlt.length; j++) {
                matrizResultante[i][j] = img.matrizImgAlt[j][i];
            }
        }
        Imagem imagem = new Imagem();
        imagem.matrizImgAlt = matrizResultante;
        return imagem;
    }

    public Imagem negativar(Imagem img) {
        int matrizResultante[][] = new int[img.matrizImgAlt.length][img.matrizImgAlt[0].length];
        for (int i = 0; i < img.matrizImgAlt.length; i++) {
            for (int j = 0; j < img.matrizImgAlt[0].length; j++) {
                if (img.matrizImgAlt[i][j] >= 128) {
                    matrizResultante[i][j] = 128 - (img.matrizImgAlt[i][j] - 128);
                }else{
                    matrizResultante[i][j] = (128 - img.matrizImgAlt[i][j]) + 128;
                }
            }
        }
        Imagem imagem = new Imagem();
        imagem.matrizImgAlt = matrizResultante;
        return imagem;
    }
}
