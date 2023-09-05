from dataclasses import dataclass, field
from functools import cached_property
from typing import Dict, List, Tuple

from aidb.config.config_types import Column, Table
from aidb.inference.inference_service import InferenceService


@dataclass
class Config:
  '''
  Data class that holds all the information required for an AIDB instance.
  Although the data class is mutable, none of the fields should be mutated externally.
  '''

  # Metadata
  db_uri: str = ''
  blob_tables: List[str] = field(default_factory=list)
  # table name -> blob key (possibly composite)
  blob_keys: Dict[str, List[str]] = field(default_factory=dict)

  # Schema
  tables: Dict[str, Table] = field(default_factory=dict)
  columns: Dict[str, Column] = field(default_factory=dict)
  relations: Dict[str, str] = field(default_factory=dict) # left -> right

  # Inference engines
  engine_by_name: Dict[str, InferenceService] = field(default_factory=dict)
  # engine name -> (inputs, outputs)
  engine_bindings: Dict[str, Tuple[List[str], List[str]]] = field(default_factory=dict)
  column_by_engine: Dict[str, InferenceService] = field(default_factory=dict)


  # TODO: figure out the type
  @cached_property
  def table_graph(self) -> Dict[str, str]:
    raise NotImplementedError()


  @cached_property
  def engine_graph(self) -> Dict[str, str]:
    raise NotImplementedError()


  # TODO: actually check validity
  def check_validity(self):
    return True