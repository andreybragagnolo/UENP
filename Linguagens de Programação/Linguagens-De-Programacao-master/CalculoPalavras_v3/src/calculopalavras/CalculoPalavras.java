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
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 *
 * @author andre
 */
public class CalculoPalavras {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        Texto text = new Texto(null, null);
        Palavras auxiliar = new Palavras();
        String texto[] = new String[100000];
        String diretorioArquivo = "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\teste.txt";
        text.setTexto(text.recebeTexto(diretorioArquivo));
        int valor = texto.length;
        ArrayList<Palavras> listaPalavras = new ArrayList<Palavras>(valor);
        text.setTamDivision(valor / 2);
        listaPalavras = text.compute();
        listaPalavras.forEach(item -> System.out.println("Palavra =" +item.getPalavra() + " Contagem ="+item.getContador()));
    }
}
