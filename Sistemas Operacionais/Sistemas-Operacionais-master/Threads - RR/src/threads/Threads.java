/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package threads;

import java.time.Instant;
import java.time.Duration;
import java.util.ArrayList;
import java.util.List;

public class Threads {

    public static void main(String[] args) throws InterruptedException {
        //Cria os objetos para medida de tempo e listas de tarefa a serem utilizadas
        Instant startTime = Instant.now();
        List<Tarefa> list = new ArrayList<Tarefa>();
        Tarefa T = new Tarefa("aux", 1000, 1, 1, 0, 0);
        list = T.restartLista();
        List<Tarefa> listaExec = new ArrayList<Tarefa>();

//      while(list.isEmpty()!=true){
//          
//      }
        Instant endTime = Instant.now();
        Duration totalTime = Duration.between(startTime, endTime);
        long duracao = totalTime.toMillis();
        while (duracao < 3000) {
            Tarefa exec = new Tarefa("exec", 0, 1, 0, 0, 0);
            if (listaExec.isEmpty() == true) {
                duracao = exec.verificaStatus(list, startTime, listaExec);

            } else {
                System.out.println("Fila de Execução: ");
                exec = exec.filaExecucao(list, duracao, listaExec);
                for (Tarefa f : listaExec) {
                    System.out.print("| Tarefa: " + f.getNomeId() + "| Pronta em: " + f.getTempoPronto()+ "ms|");
                }
                System.out.println("");
                if (exec != null) {
                    duracao = exec.execucaoTarefa(exec, startTime, listaExec, list);
                    duracao = exec.verificaStatus(list, startTime, listaExec);
                } else {

                }

            }

        }

    }

}
