import type { Product } from "@/product";

var indexedDB = window.indexedDB;
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

            objectStore.createIndex("person", "person", { unique: false });
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
    if (!database) {
        console.error("DB NOT OPEN")
    }
    console.log(database)
    let transaction = database.transaction("products", "readwrite")
    let objectStore = transaction.objectStore("products")
    let req = objectStore.add(product)
    req.onsuccess = function (event: any) {
        console.log("Product Added ", event.target.result)
    }
    req.onerror = function (event: any) {
        console.error("Chef il y a une erreur ", event.target.errorCode);
    }
}

export async function deleteProductInDB(product: string) {
    if (!database) {
        console.error("DB NOT OPEN")
    }
    console.log(database)
    let req = database.transaction("products", "readwrite").objectStore("products").delete(product)
    req.onsuccess = function (event: any) {
        console.log("supprimé")
    }

}

export async function getProductsInDB(): Promise<Product[]> {
    if (!database) {
        console.error("DB NOT OPEN")
    }
    console.log(database)
    return new Promise<Product[]>((resolve, reject) => {
        const req = database.transaction("products", "readwrite").objectStore("products").getAll()
        req.onsuccess = function () {
            console.log(req.result)
            resolve(req.result as Product[])
        }
        req.onerror = function (event: any) {
            console.error("Erreur récupération produits :", event.target.errorCode)
            reject(event.target.errorCode)
        }
    })
}

export async function updateProductInDB(product: Product) {
    if (!database) {
        console.error("DB NOT OPEN")
    }
    console.log(database)
    let objectStore = database
        .transaction(["products"], "readwrite")
        .objectStore("products");
    const req = objectStore.get(product.id)
    req.onsuccess = function () {
        let requestUpdate = objectStore.put(product);
        requestUpdate.onerror = function (event) {
            // Faire quelque chose avec l’erreur
        };
        requestUpdate.onsuccess = function (event) {
            console.log('Modifié')
        };

    }
    req.onerror = function (event: any) {
        console.error("Erreur récupération produits :", event.target.errorCode)

    }

}

export async function getTotalProductsInDB(){
    if (!database) {
        console.error("DB NOT OPEN")
    }
    console.log(database)
    return new Promise<number>((resolve, reject) => {
        const req = database.transaction("products", "readwrite").objectStore("products").getAll()
        req.onsuccess = function () {
            let res:number=0 ;
            let data = req.result as Product[]
            data.forEach(p => res += p.price )
            resolve(res)
        }
        req.onerror = function (event: any) {
            console.error("Erreur récupération produits :", event.target.errorCode)
            reject(event.target.errorCode)
        }
    })
}