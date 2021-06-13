/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package paralelismo;

import java.util.concurrent.RecursiveTask;
import java.util.Random;

/**
 *
 * @author andre
 */
public class EncontrarVogais extends RecursiveTask<Integer> {

    private String texto;
    static int TamMax = 10000000;

    public String getTexto() {
        return texto;
    }

    public void setTexto(String texto) {
        this.texto = texto;
    }

    private static int encontrarVogais(String texto) {
        int contadorVog = 0;

        texto.toLowerCase();

        for (int i = 0; i < texto.length(); i++) {
            char c = texto.charAt(i);
            if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                contadorVog++;
            }
        }
        return contadorVog;
    }

    public int calcularVogais(String texto) {
        int contadorVog = 0;

        texto.toLowerCase();

        for (int i = 0; i < texto.length(); i++) {
            char c = texto.charAt(i);
            if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                contadorVog++;
            }
        }
        System.out.println("Contador =" + contadorVog);
        return contadorVog;

    }

    @Override
    protected Integer compute() {
        if (texto.length() > TamMax) {
            return this.encontrarVogais(texto);
        }

        EncontrarVogais trecho1 = new EncontrarVogais(texto.substring(0, TamMax - 1));
        EncontrarVogais trecho2 = new EncontrarVogais(texto.substring(TamMax));
        trecho1.fork();
        trecho2.fork();
        int trecho1Resultado = trecho1.join();
        int trecho2Resultado = trecho2.join();
        return trecho1Resultado + trecho2Resultado;
    }

    public EncontrarVogais(String texto) {
        this.texto = texto;
    }

    public String geradorDeTexto() {
        Random random = new Random();
        String textoGerado = new String();
        char[] vetorchar = new char[20000000];
        String letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        for (int i = 0; i < 20000000; i++) {
            int valor = random.nextInt(25);
            textoGerado = textoGerado + "" + letras.charAt(valor);
        }
        return textoGerado;
    }
}
