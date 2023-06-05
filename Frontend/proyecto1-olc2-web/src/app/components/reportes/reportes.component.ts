import { Component } from '@angular/core';
import { graphviz }  from 'd3-graphviz';

@Component({
  selector: 'app-reportes',
  templateUrl: './reportes.component.html',
  styleUrls: ['./reportes.component.css']
})
export class ReportesComponent {
  
  reporteAst(){
    graphviz("#ast")
    .renderDot('digraph {a -> b}');
  }
}
