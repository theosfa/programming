using System.Xml;
using System;

namespace xmlCode{
    class test{
        // public static void Main(String[] args){
        //     XmlDocument peopleXML = new XmlDocument();
        //     peopleXML.Load("people.xml");
        //     // получим корневой элемент
        //     XmlElement? xRoot = peopleXML.DocumentElement;
        //     if (xRoot != null)
        //     {
        //         // обход всех узлов в корневом элементе
        //         foreach (XmlElement xnode in xRoot)
        //         {
        //             // получаем атрибут name
        //             XmlNode? attr = xnode.Attributes.GetNamedItem("name");
        //             if (attr?.Value != null){
        //                 Console.WriteLine(attr?.Value);
        //             }else{
        //                 Console.WriteLine("Brak <name>");
        //             }
                    
                    
        //             // обходим все дочерние узлы элемента user
        //             foreach (XmlNode childnode in xnode.ChildNodes)
        //             {
        //                 if(xnode.ChildNodes.Count == 1){
        //                     if (childnode.Name == "company")
        //                     {
        //                         Console.WriteLine($"Company: {childnode.InnerText}");
        //                         Console.WriteLine("Brak <age>");
        //                     }
        //                     if (childnode.Name == "age")
        //                     {
        //                         Console.WriteLine("Brak <company>");
        //                         Console.WriteLine($"Age: {childnode.InnerText}");
        //                     }
        //                 }else{
        //                     if (childnode.Name == "company")
        //                         {
        //                             Console.WriteLine($"Company: {childnode.InnerText}");
                                    
        //                         }
        //                     if (childnode.Name == "age")
        //                     {
        //                         Console.WriteLine($"Age: {childnode.InnerText}");
                                
        //                     }
        //                 }
                        
        //             }
        //             Console.WriteLine();
        //         }
        //     }
        // }
    }
}