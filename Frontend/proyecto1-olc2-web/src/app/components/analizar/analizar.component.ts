import { Component, Input } from '@angular/core';
import { CodeModel } from '@ngstack/code-editor';
import { GeneralServiceService } from 'src/app/services/general-service.service';

@Component({
  selector: 'app-analizar',
  templateUrl: './analizar.component.html',
  styleUrls: ['./analizar.component.css']
})
export class AnalizarComponent {
  codigo:any = "";
  theme = 'vs-dark';
  consola = "";

  constructor(private servicio: GeneralServiceService){
    this.codigo = ""
  }

  codeModel: CodeModel = {
    language: 'typescript',
    uri: 'main.ts',
    value: ""
  };

  options = {
    contextmenu: true,
    minimap: {
      enabled: true
    }
  };

  ejecutar(){

    if(this.codeModel.value != "" && this.codeModel.value != null && this.codeModel.value != undefined){
      let datos = {  
        textoEntrada: this.codeModel.value
      };
      let stringifiedData = JSON.stringify(datos);
      this.servicio.mandarCodigo(stringifiedData).subscribe(
        (response:any) =>{
          console.log(response)
          this.consola = response.textoSalida
        }
      )
    }
    console.log(this.codeModel.value);
  }
}
