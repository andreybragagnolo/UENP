/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package threads;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.time.Instant;
import java.time.Duration;

public class Tarefa extends Thread {

    private String nomeId;
    private long tempoPronto;
    private int status;
    private int flagExec;
    private int contadorExec;
    private int prioridade;
    //flagExec mostra se a tarefa foi executada ou não 1- sim, 0-não.
    //status é para monitorar se a tarefa está pronta ou não 

    public int getContadorExec() {
        return contadorExec;
    }

    public void setContadorExec(int contadorExec) {
        this.contadorExec = contadorExec;
    }

    public int getFlagExec() {
        return flagExec;
    }

    public void setFlagExec(int flagExec) {
        this.flagExec = flagExec;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public Tarefa(String nome, int tempoPronto, int prioridade, int status, int flagExec, int contadorExec) {
        this.nomeId = nome;
        this.tempoPronto = tempoPronto;
        this.prioridade = prioridade;
        this.status = status;
        this.flagExec = flagExec;
        this.contadorExec = contadorExec;
    }

    public String getNomeId() {
        return nomeId;
    }

    public long getTempoPronto() {
        return tempoPronto;
    }

    public long execucaoTarefa(Tarefa t, Instant inicio, List<Tarefa> listaExec, List<Tarefa> list) {
        if (listaExec.contains(t)) {
            Instant intermediario = Instant.now();
            Duration totalTime = Duration.between(inicio, intermediario);
            long contador = totalTime.toMillis();
            long aux = contador;
            t.printTarefa(t, contador);
            while ((contador) != aux + 30) {
                intermediario = Instant.now();
                totalTime = Duration.between(inicio, intermediario);
                contador = totalTime.toMillis();
            }
            listaExec.remove(t);

            for (Tarefa f : list) {
                if (f.getNomeId() == t.getNomeId() && f.getContadorExec() < 2) {
                    List<Tarefa> copia = new ArrayList<Tarefa>();
                    copia = restartLista();
                    f.setStatus(0);
                    f.setFlagExec(0);
                    f.setContadorExec(f.getContadorExec() + 1);
                    for(Tarefa copy : copia){
                        if (f.getNomeId()==copy.getNomeId()){
                            f.setPrioridade(copy.getPrioridade());
//                            System.out.println("Prioridade ="+f.getPrioridade());
                        }
                    }
                }
            }
            for (Tarefa f : listaExec) {

                f.mudaPrioridade(f);

            }

            return contador;
        } else {
            Instant intermediario = Instant.now();
            Duration totalTime = Duration.between(inicio, intermediario);
            long contador = totalTime.toMillis();
            return contador;
        }

    }

    public int getPrioridade() {
        return prioridade;
    }

    public void setPrioridade(int prioridade) {
        this.prioridade = prioridade;
    }

    public void mudaPrioridade(Tarefa t) {
        t.setPrioridade(t.getPrioridade() + 1);
    }

    public long verificaStatus(List<Tarefa> list, Instant startTime, List<Tarefa> listaExec) {
        Instant endtime = Instant.now();
        Duration totalTime = Duration.between(startTime, endtime);
        long duracao = totalTime.toMillis();
        for (Tarefa t : list) {
            if ((duracao >= t.getTempoPronto()) && (t.getFlagExec() == 0) && (list.contains(t) && (listaExec.contains(t) != true))) {
                t.setStatus(1);
                listaExec.add(t);
            }
        }
        return duracao;
    }

    public void printTarefa(Tarefa t, long contador) {
        System.out.println("-------------------------------");
        System.out.println("EXECUTANDO A TAREFA:" + t.getNomeId() + "| No tempo:" + contador + " |Com PRIORIDADE: " + t.getPrioridade() + " |Tempo PRONTO :" + t.getTempoPronto());
        System.out.println("_______________________________");
    }

    public Tarefa filaExecucao(List<Tarefa> list, long duracao, List<Tarefa> listaExec) {

        Tarefa auxiliar = new Tarefa("aux", 1000, 1, 1, 0, 0);
        for (Tarefa t : listaExec) {
            if ((t.getPrioridade() >= auxiliar.getPrioridade()) && (t.getTempoPronto() <= duracao) && (t.getStatus() == 1) && (t.getFlagExec() == 0)) {
                auxiliar = t;
            }
        }
        for (Tarefa t : list) {
            if (t.getNomeId() == auxiliar.getNomeId()) {
                t.setFlagExec(1);

//                System.out.println("Executada a tarefa:" + t.getNomeId() + "| No tempo:" + duracao);
            }
        }
        return auxiliar;
    }

    public List<Tarefa> restartLista() {
        List<Tarefa> list = new ArrayList<Tarefa>();
        Tarefa tarefa1 = new Tarefa("t1", 300, 3, 0, 0, 0);
        Tarefa tarefa2 = new Tarefa("t2", 250, 2, 0, 0, 0);
        Tarefa tarefa3 = new Tarefa("t3", 100, 5, 0, 0, 0);
        Tarefa tarefa4 = new Tarefa("t4", 200, 8, 0, 0, 0);
        Tarefa tarefa5 = new Tarefa("t5", 250, 3, 0, 0, 0);
        Tarefa tarefa6 = new Tarefa("t6", 150, 1, 0, 0, 0);
        Tarefa tarefa7 = new Tarefa("t7", 100, 1, 0, 0, 0);
        Tarefa tarefa8 = new Tarefa("t8", 200, 4, 0, 0, 0);
        Tarefa tarefa9 = new Tarefa("t9", 300, 6, 0, 0, 0);
        Tarefa tarefa0 = new Tarefa("t0", 200, 1, 0, 0, 0);

        list.add(tarefa1);
        list.add(tarefa2);
        list.add(tarefa3);
        list.add(tarefa4);
        list.add(tarefa5);
        list.add(tarefa6);
        list.add(tarefa7);
        list.add(tarefa8);
        list.add(tarefa9);
        list.add(tarefa0);

        return list;
    }

    @Override
    public void run() {
//        System.out.println("Executando a tarefa:" + getNomeId());

    }

}
