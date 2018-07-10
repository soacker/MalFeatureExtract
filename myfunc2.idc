#include <idc.idc>

static main()
{
  auto file,asm_file,gdl_file;

  // turn on coagulation of data in the final pass of analysis
  SetShortPrm(INF_AF2, GetShortPrm(INF_AF2) | AF2_DODATA);

  Message("Waiting for the end of the auto analysis...\n");
  Wait();

  Message("\n\n------ Creating the output file.... --------\n");
  file = GetIdbPath();
  asm_file = substr(file,0,strstr(file,".")) + ".asm";
  WriteTxt(asm_file, 0, BADADDR);           // create the assembler file

  gdl_file = substr(file,0,strstr(file,".")) + ".gdl";
  GenFuncGdl(gdl_file, "Call Gdl", CHART_GEN_GDL);
  SaveBase(gdl_file,0);
  //WriteTxt(gdl_file, 0, BADADDR); 







  Message("All done, exiting...\n");
  Exit(0);                              // exit to OS, error code 0 - success
}
