/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculopalavras;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.RecursiveTask;
import java.util.stream.Stream;
import java.util.Collection;


/**
 *
 * @author andre
 */
public class Texto extends RecursiveTask<ArrayList> {

    private ArrayList<Palavras> texto;
    private ArrayList<Palavras> palavras;
    private ArrayList<Palavras> stopwords;
    private int TamDivision;

    public int getTamDivision() {
        return TamDivision;
    }

    public void setTamDivision(int TamDivision) {
        this.TamDivision = TamDivision;
    }

    public Texto(ArrayList<Palavras> texto, ArrayList<Palavras> palavras) {
        this.texto = texto;
        this.palavras = palavras;
        this.stopwords = stopwords;
    }
    

    public ArrayList<Palavras> recebeTexto(String diretorio) throws FileNotFoundException, IOException {
        String texto;
        texto = "";
        String linha = "";
        FileReader read = new FileReader(diretorio);
        BufferedReader buffer = new BufferedReader(read);
        while ((linha = buffer.readLine()) != null) {
            texto = texto.replace(texto, texto + linha + " ");
        }
        texto = removePontuacao(texto);
        String[] spliter = texto.toUpperCase().split(" ");
        ArrayList<Palavras> listPalavras = new ArrayList<>(texto.length());
        ArrayList<String> stopwords = recebeStopWords("C:\\Users\\andre\\OneDrive\\Área de Trabalho\\Stopwords.txt");
        String[] textoNoStopWord = deletaStopWords(spliter, stopwords);
        for (String item : textoNoStopWord) {
            Palavras p = new Palavras();
            p.setPalavra(item);
            listPalavras.add(p);
        }

        return listPalavras;
    }

    public static ArrayList<String> recebeStopWords(String diretorio) throws FileNotFoundException, IOException {
        String texto = "";
        String linha = "";
        FileReader read = new FileReader(diretorio);
        BufferedReader buffer = new BufferedReader(read);
        while ((linha = buffer.readLine()) != null) {
            texto = texto.replace(texto, texto + linha + " ");
        }
        String[] spliter = texto.toUpperCase().split(" ");
        ArrayList<String> listPalavras = new ArrayList<>(texto.length());
        for (String item : spliter) {
            listPalavras.add(item);
        }
        return listPalavras;
    }

    public static String[] deletaStopWords(String[] texto, ArrayList<String> stopwords) {
      return Arrays.stream(texto)
                .filter(i -> stopwords.contains(i)!=true)
                .map(Upercase -> Upercase.toUpperCase())
                .toArray(String[]::new);       
         
    }
    
    public static String[] deletaDuplicata(String[] texto) {
        return Arrays.stream(texto).distinct().toArray(String[]::new);
         
    }

    public ArrayList<Palavras> getTexto() {
        return texto;
    }

    public void setTexto(ArrayList<Palavras> texto) {
        this.texto = texto;
    }

    public ArrayList<Palavras> getPalavras() {
        return palavras;
    }

    public void setPalavras(ArrayList<Palavras> palavras) {
        this.palavras = palavras;
    }

    public ArrayList<Palavras> getStopwords() {
        return stopwords;
    }

    public void setStopwords(ArrayList<Palavras> stopwords) {
        this.stopwords = stopwords;
    }

    public String removePontuacao(String texto) {

        String semPontuacao = texto.replace('?', ' ');
        semPontuacao = semPontuacao.replace(',', ' ');
        semPontuacao = semPontuacao.replace('.', ' ');
        semPontuacao = semPontuacao.replace('!', ' ');
        semPontuacao = semPontuacao.replace("  ", " ");

        return semPontuacao;
    }


    public static ArrayList<Palavras> verificadorFrequencia(ArrayList<Palavras> texto, int valor) {
        ArrayList<Palavras> vetorPalavras = new ArrayList<>(valor);
        String[] vetor = new String[texto.size()];
        int i=0;
        for (Palavras item : texto){
            vetor[i] = item.getPalavra();
            i++;
        }
        String[] conversao = deletaDuplicata(vetor);
        for(String item: conversao){
        Palavras p = new Palavras();
        p.setPalavra(item);
        vetorPalavras.add(p);
        }
        for (Palavras itemVP : vetorPalavras){
            int quantidade = 0;
            for (Palavras itemTexto : texto){
                if(itemVP.getPalavra().equals(itemTexto.getPalavra())){
                    Palavras p = new Palavras();
                    quantidade = (itemVP.getContador()+1);
                    itemVP.setContador(quantidade);
                }else{
                }
            }
        }
//        int quantidade = 0;
//        boolean contem = false;
//        for (Palavras item : texto) {
//            contem = false;
//            Palavras auxiliar = new Palavras();
//            auxiliar.setPalavra(item.getPalavra());
//            for (Palavras p : vetorPalavras) {
//                if (p != null) {
//                    if (p.getPalavra().equals(auxiliar.getPalavra())) {
//                        contem = true;
//                        auxiliar = p;
//                    }
//                }
//            }
//            if (contem == true) {
//                quantidade = (auxiliar.getContador() + 1);
//                auxiliar.setContador(quantidade);
//            } else {
//                auxiliar.setPalavra(item.getPalavra());
//                auxiliar.setContador(1);
//                vetorPalavras.add(auxiliar);
//            }
//        }
        return vetorPalavras;
    }

    @Override
    protected ArrayList compute() {

        if (texto.size() <= TamDivision) {
            return this.verificadorFrequencia(texto, TamDivision);
        }
        new ArrayList<Palavras>(texto.subList(0, TamDivision));

        Texto trecho1 = new Texto(new ArrayList<Palavras>(texto.subList(0, TamDivision - 1)), palavras);
        Texto trecho2 = new Texto(new ArrayList<Palavras>(texto.subList(TamDivision, texto.size())), palavras);
        trecho1.fork();
        trecho2.fork();
        ArrayList<Palavras> trecho1Resultado = trecho1.join();
        ArrayList<Palavras> trecho2Resultado = trecho2.join();
        ArrayList<Palavras> listaFinal = new ArrayList<>();
        for (Palavras p : trecho1Resultado) {
            listaFinal.add(p);
        }
        for (Palavras p : trecho2Resultado) {
            listaFinal.add(p);
        }
        return listaFinal;
    }

}
