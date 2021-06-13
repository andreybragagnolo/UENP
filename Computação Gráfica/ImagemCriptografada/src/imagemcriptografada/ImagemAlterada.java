/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package imagemcriptografada;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.awt.image.Raster;
import java.awt.image.RenderedImage;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.util.Iterator;
import java.util.Random;
import javax.imageio.*;

/**
 *
 * /**
 *
 * @author andy_
 */
public class ImagemAlterada {

    public static void main(String[] args) throws IOException {
        Imagem img = new Imagem();
        int matrizImagem[][] = null;
        matrizImagem = img.recebeImagem();
        System.out.println("Resolucao =" + matrizImagem.length / 3 + " x " + matrizImagem[0].length);
        BufferedImage imgBuff = null;
        imgBuff = new BufferedImage(matrizImagem.length / 3, (matrizImagem[0].length), imgBuff.TYPE_INT_ARGB);

        for (int itemLarg = 0; itemLarg < matrizImagem.length / 3; itemLarg++) {
            for (int itemAlt = 0; itemAlt < matrizImagem[0].length; itemAlt++) {
                Color c = new Color(matrizImagem[itemLarg * 3][itemAlt], matrizImagem[itemLarg * 3 + 1][itemAlt], matrizImagem[itemLarg * 3 + 2][itemAlt]);
                imgBuff.setRGB(itemLarg, itemAlt, c.getRGB());
            }
        }
        boolean writer = ImageIO.write((RenderedImage) imgBuff, "png", new File("Original.png"));
        Imagem alterada = img.ImagemSomaMatrizes(matrizImagem, 200);

        for (int itemLarg = 0; itemLarg < alterada.matrizImgAlt.length / 3; itemLarg++) {
            for (int itemAlt = 0; itemAlt < alterada.matrizImgAlt[0].length; itemAlt++) {

                if ((alterada.matrizImgAlt[itemLarg * 3 + 1][itemAlt] >= 0) && (alterada.matrizImgAlt[itemLarg * 3 + 2][itemAlt] >= 0) && (alterada.matrizImgAlt[itemLarg * 3][itemAlt] >= 0) && (alterada.matrizImgAlt[itemLarg * 3][itemAlt] <= 255) && (alterada.matrizImgAlt[itemLarg * 3 + 1][itemAlt] <= 255) && (alterada.matrizImgAlt[itemLarg * 3 + 2][itemAlt] <= 255)) {
                    Color c = new Color(alterada.matrizImgAlt[itemLarg * 3][itemAlt], alterada.matrizImgAlt[itemLarg * 3 + 1][itemAlt], alterada.matrizImgAlt[itemLarg * 3 + 2][itemAlt]);
                    imgBuff.setRGB(itemLarg, itemAlt, c.getRGB());
                } else {
                    int r, g, b;
                    r = alterada.matrizImgAlt[itemLarg * 3][itemAlt];
                    g = alterada.matrizImgAlt[itemLarg * 3 + 1][itemAlt];
                    b = alterada.matrizImgAlt[itemLarg * 3 + 2][itemAlt];

                    if (alterada.matrizImgAlt[itemLarg * 3 + 1][itemAlt] < 0) {
                        g = 0;
                    }
                    if (alterada.matrizImgAlt[itemLarg * 3 + 1][itemAlt] > 255) {
                        g = 255;
                    }
                    if (alterada.matrizImgAlt[itemLarg * 3 + 2][itemAlt] > 255) {
                        b = 255;
                    }
                    if (alterada.matrizImgAlt[itemLarg * 3 + 2][itemAlt] < 0) {
                        b = 0;
                    }
                    if (alterada.matrizImgAlt[itemLarg * 3][itemAlt] < 0) {
                        r = 0;
                    }
                    if (alterada.matrizImgAlt[itemLarg * 3][itemAlt] > 255) {
                        r = 255;
                    }
                    Color c = new Color(r, g, b);
                    imgBuff.setRGB(itemLarg, itemAlt, c.getRGB());
                }
            }
        }

        writer = ImageIO.write((RenderedImage) imgBuff, "png", new File("Alterada.png"));
        Imagem normalizada = img.ReverteSomaMatrizes(alterada);
        for (int itemLarg = 0; itemLarg < alterada.matrizImgAlt.length / 3; itemLarg++) {
            for (int itemAlt = 0; itemAlt < alterada.matrizImgAlt[0].length; itemAlt++) {
                int r, g, b;

                r = normalizada.matrizImgAlt[itemLarg * 3][itemAlt];
                g = normalizada.matrizImgAlt[itemLarg * 3 + 1][itemAlt];
                b = normalizada.matrizImgAlt[itemLarg * 3 + 2][itemAlt];
                if (r == 0 || g == 0 || b == 0) {
                    Color c = new Color(0, 255, 0);
                    imgBuff.setRGB(itemLarg, itemAlt, c.getRGB());
                } else {
                    Color c = new Color(r, g, b);
                    imgBuff.setRGB(itemLarg, itemAlt, c.getRGB());
                }
            }
        }
        writer = ImageIO.write((RenderedImage) imgBuff, "png", new File("Normalizada.png"));

        Imagem tonalidade = new Imagem();
        img.matrizImgAlt = matrizImagem;
        tonalidade = img.ImagemMultiplicaEscalar(img, 5);

        for (int itemLarg = 0; itemLarg < tonalidade.matrizImgAlt.length / 3; itemLarg++) {
            for (int itemAlt = 0; itemAlt < tonalidade.matrizImgAlt[0].length; itemAlt++) {

                if ((tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt] >= 0) && (tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt] >= 0) && (tonalidade.matrizImgAlt[itemLarg * 3][itemAlt] >= 0) && (tonalidade.matrizImgAlt[itemLarg * 3][itemAlt] <= 255) && (tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt] <= 255) && (tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt] <= 255)) {
                    Color c = new Color(tonalidade.matrizImgAlt[itemLarg * 3][itemAlt], tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt], tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt]);
                    imgBuff.setRGB(itemLarg, itemAlt, c.getRGB());
                } else {
                    int r, g, b;
                    r = tonalidade.matrizImgAlt[itemLarg * 3][itemAlt];
                    g = tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt];
                    b = tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt];

                    if (tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt] < 0) {
                        g = 0;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt] > 255) {
                        g = 255;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt] > 255) {
                        b = 255;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt] < 0) {
                        b = 0;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3][itemAlt] < 0) {
                        r = 0;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3][itemAlt] > 255) {
                        r = 255;
                    }
                    Color c = new Color(r, g, b);
                    imgBuff.setRGB(itemLarg, itemAlt, c.getRGB());
                }

            }
        }
        writer = ImageIO.write((RenderedImage) imgBuff, "png", new File("Tonalidade.png"));
        tonalidade = img.ImagemDivideEscalar(img, 3);

        for (int itemLarg = 0; itemLarg < tonalidade.matrizImgAlt.length / 3; itemLarg++) {
            for (int itemAlt = 0; itemAlt < tonalidade.matrizImgAlt[0].length; itemAlt++) {

                if ((tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt] >= 0) && (tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt] >= 0) && (tonalidade.matrizImgAlt[itemLarg * 3][itemAlt] >= 0) && (tonalidade.matrizImgAlt[itemLarg * 3][itemAlt] <= 255) && (tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt] <= 255) && (tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt] <= 255)) {
                    Color c = new Color(tonalidade.matrizImgAlt[itemLarg * 3][itemAlt], tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt], tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt]);
                    imgBuff.setRGB(itemLarg, itemAlt, c.getRGB());
                } else {
                    int r, g, b;
                    r = tonalidade.matrizImgAlt[itemLarg * 3][itemAlt];
                    g = tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt];
                    b = tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt];

                    if (tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt] < 0) {
                        g = 0;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3 + 1][itemAlt] > 255) {
                        g = 255;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt] > 255) {
                        b = 255;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3 + 2][itemAlt] < 0) {
                        b = 0;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3][itemAlt] < 0) {
                        r = 0;
                    }
                    if (tonalidade.matrizImgAlt[itemLarg * 3][itemAlt] > 255) {
                        r = 255;
                    }
                    Color c = new Color(r, g, b);
                    imgBuff.setRGB(itemLarg, itemAlt, c.getRGB());
                }

            }
        }
        writer = ImageIO.write((RenderedImage) imgBuff, "png", new File("Tonalidade2.png"));

        Imagem transposta = new Imagem();
        transposta = img.transpor(img);
        BufferedImage imgBuff2 = null;
        imgBuff2 = new BufferedImage(matrizImagem[0].length, matrizImagem.length / 3, imgBuff2.TYPE_INT_ARGB);
        for (int i = 0; i < transposta.matrizImgAlt[0].length / 3; i++) {
            for (int j = 0; j < transposta.matrizImgAlt.length; j++) {

                int r, g, b;
                r = transposta.matrizImgAlt[j][i * 3];
                g = transposta.matrizImgAlt[j][i * 3 + 1];
                b = transposta.matrizImgAlt[j][i * 3 + 2];

                Color c = new Color(r, g, b);
                imgBuff2.setRGB(j, i, c.getRGB());
            }

        }
        writer = ImageIO.write((RenderedImage) imgBuff2, "png", new File("Transposta.png"));

        Imagem negativa = new Imagem();
        negativa = img.negativar(img);
        System.out.println("Resolucao =" + negativa.matrizImgAlt.length / 3 + " x " + negativa.matrizImgAlt[0].length);
        for (int i = 0; i < negativa.matrizImgAlt.length/3; i++) {
            for (int j = 0; j < negativa.matrizImgAlt[0].length ; j++) {

                int r, g, b;
                r = negativa.matrizImgAlt[i * 3][j];
                g = negativa.matrizImgAlt[i * 3 + 1][j];
                b = negativa.matrizImgAlt[i * 3 + 2][j];

                if (g < 0) {
                    g = 0;
                }
                if (g > 255) {
                    g = 255;
                }
                if (b > 255) {
                    b = 255;
                }
                if (b < 0) {
                    b = 0;
                }
                if (r < 0) {
                    r = 0;
                }
                if (r > 255) {
                    r = 255;
                }

                Color c = new Color(r, g, b);
                imgBuff.setRGB(i, j, c.getRGB());
            }

        }
        writer = ImageIO.write((RenderedImage) imgBuff, "png", new File("Negativa.png"));
    }

}
