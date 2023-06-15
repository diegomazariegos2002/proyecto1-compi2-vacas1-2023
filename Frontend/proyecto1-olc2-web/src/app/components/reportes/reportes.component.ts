import { Component } from '@angular/core';
import { graphviz }  from 'd3-graphviz';
import { GeneralServiceService } from 'src/app/services/general-service.service';

@Component({
  selector: 'app-reportes',
  templateUrl: './reportes.component.html',
  styleUrls: ['./reportes.component.css']
})
export class ReportesComponent {
  constructor(private servicio: GeneralServiceService){
  }
  
  reporteAst(){
    this.servicio.recibirAst().subscribe(
      (response:any) =>{
        if (response){
          graphviz("#ast")
          .renderDot(response.repoast);
        }
      }
    )
  }

  reporteErrores(){
    this.servicio.recibirErrores().subscribe(
      (response:any) =>{
        let errores:any = document.querySelector('#rep-errores');
        if (response){
          errores.innerHTML = response.repoerrores
        }
      }
    )
  }

  reporteSimbolos(){
    this.servicio.recibirSimbolos().subscribe(
      (response:any) =>{
        console.log(response)
        let simbolos:any = document.querySelector('#rep-simbolos');
        if (response){
          simbolos.innerHTML = response.reposimbolos
        }
      }
    )
  }
}
