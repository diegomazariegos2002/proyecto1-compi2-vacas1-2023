import { Component, Input } from '@angular/core';
import { CodeModel } from '@ngstack/code-editor';

@Component({
  selector: 'app-analizar',
  templateUrl: './analizar.component.html',
  styleUrls: ['./analizar.component.css']
})
export class AnalizarComponent {
  codigo:any = "";
  theme = 'vs-dark';

  constructor(){
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
    console.log(this.codeModel.value);
  }
}
