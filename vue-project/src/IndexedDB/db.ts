import type { Product } from "@/product";

var indexedDB = window.indexedDB || window.mozIndexedDB || window.webkitIndexedDB || window.msIndexedDB || window.shimIndexedDB;
let database: IDBDatabase

export function openDB(): Promise<IDBDatabase> {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open("myDatabase", 3);

        request.onsuccess = function (event: any) {
            database = event.target.result; 
            console.log("DB connectée");
            resolve(database);
        };

        request.onerror = function (event: any) {
            console.error("Erreur DB : ", event.target.errorCode);
            reject(event.target.errorCode);
        };

        request.onupgradeneeded = function (event: any) {
            const db: IDBDatabase = event.target.result;
            const objectStore = db.createObjectStore("products", { keyPath: "id" });

            objectStore.createIndex("name", "name", { unique: false });
            objectStore.createIndex("price", "price", { unique: false });
            objectStore.createIndex("product", "product", { unique: false });
            objectStore.createIndex("place", "place", { unique: false });

            objectStore.transaction.oncomplete = function () {
                console.log("Structure créée");
            };
        };
    });
}





export async function addProductInDB(product: Product) {
    if (!database){
        console.error("DB NOT OPEN")
    }
    console.log(database)
    var transaction = database.transaction("products", "readwrite")
    var objectStore = transaction.objectStore("products")
    var req = objectStore.add(product)
    req.onsuccess = function (event: any) {
        console.log("Product Added ", event.target.result)
    }
    req.onerror = function (event: any) {
        console.error("Chef il y a une erreur ", event.target.errorCode);
    }
}