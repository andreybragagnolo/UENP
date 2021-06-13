/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculopalavras;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;

/**
 *
 * @author andre
 */
public class CalculoPalavras {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        Texto text = new Texto(null, null, null);
        Palavras auxiliar = new Palavras();
        String texto[] = new String[100000];
        String diretorioArquivo = "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\teste.txt";
        text.setTexto(text.recebeTexto(diretorioArquivo));
        int valor = texto.length;
        ArrayList<Palavras> listaPalavras = new ArrayList<Palavras>(valor);
        ArrayList<Palavras> stopwords = new ArrayList<Palavras>(50);
        stopwords = text.verificaStopWords(stopwords);
        Instant Start = Instant.now();
        listaPalavras = text.verificadorFrequencia(text.getTexto(), valor, stopwords);
        Instant End = Instant.now();
        Duration total = Duration.between(Start, End);
        long totalms = total.toMillis();
        System.out.println("Duração Tarefa Sequencial =" + totalms + "ms");
        for (Palavras item : listaPalavras) {
            System.out.println("Palavra =" + item.getPalavra() + "| Contador=" + item.getContador());
        }
        text.setTexto(text.recebeTexto(diretorioArquivo));
        text.setStopwords(stopwords);
        for (int i = 0; i < 15; i++) {
            System.out.println("--------------------");
        }
        text.setTamDivision(valor / 2);
        Start = Instant.now();
        listaPalavras = text.compute();
        End = Instant.now();
        total = Duration.between(Start, End);
        totalms = total.toMillis();
        System.out.println("Duração Tarefa Paralela =" + totalms + "ms");
        System.out.println("------Iniciando Paralelismo --------");
        for (Palavras item : listaPalavras) {
            System.out.println("Palavra =" + item.getPalavra() + "| Contador=" + item.getContador());
        }

    }
}
