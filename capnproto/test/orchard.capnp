@0x92091441d6d48952;

using Flower = import "flower.capnp";
using Power = UInt64;

struct Tree {
  fruit @0 :List(Fruit);
  branch @1 :List(Branch);
}

enum Fruit
{
  apple @0;
  orange @1;
}

struct Branch
{
  branches @0 :Tree;

  union {
    bare @2 :Void;
    budding: group {
      flower @1 : Flower.Petal;
      sap @4 :UInt8;
    }
    flowering : group {
      flower @5 : Flower.Petal;
      power @6 :Power;
    }
  }
  length @3 :UInt16;
}
