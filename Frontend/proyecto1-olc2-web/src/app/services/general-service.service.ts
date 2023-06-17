import { Injectable } from '@angular/core';
import { Observable, lastValueFrom } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class GeneralServiceService {

  constructor(private http:HttpClient) { }

  mandarCodigo(codigo:any){
    let httpOptions = {
      headers: new HttpHeaders({
        'Content-type':'application/json'
      })
    }
    return this.http.post<any>("/proyectoolc2/analizar", codigo, httpOptions).pipe(
      catchError(e => {console.log(e)
        return ""
      })
    );
  }

  mandarCodigoTraducir(codigo:any){
    let httpOptions = {
      headers: new HttpHeaders({
        'Content-type':'application/json'
      })
    }
    return this.http.post<any>("/proyectoolc2/generarCodigo", codigo, httpOptions).pipe(
      catchError(e => {console.log(e)
        return ""
      })
    );
  }

  recibirErrores(){
    return this.http.get('/proyectoolc2/errores').pipe(
      catchError(e => e.toString())
    );
  }

  recibirSimbolos(){
    return this.http.get('/proyectoolc2/simbolos').pipe(
      catchError(e => e.toString())
    );
  }

  recibirAst(){
    return this.http.get('/proyectoolc2/ast').pipe(
      catchError(e => e.toString())
    );
  }
}
