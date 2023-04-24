from .Pipeline import Pipeline
from .implementations import *


def build_pipeline(practice: bool, solution: bool, teaching: bool,
                   remove_without_macros: bool, remove_empty: bool,
                   strip_lines: bool, remove_trailing_lines: bool,
                   embed_images: bool,
                   force_readonly: bool, force_undeletable: bool,
                   remove_output: bool) -> Pipeline:
    pipeline = Pipeline()

    pipeline.add(SplitSource())

    pipeline.add(RemoveCellByMacro(practice, solution, teaching, remove_without_macros))
    pipeline.add(RemovePyCharm())

    pipeline.add(TableOfContents())

    pipeline.add(SetReadonly(force_readonly))

    if force_undeletable:
        pipeline.add(SetUndeletable())

    pipeline.add(RemoveMacrosFromCode())
    pipeline.add(RemoveMacrosFromTags())

    if strip_lines:
        pipeline.add(StripLines())

    if remove_trailing_lines:
        pipeline.add(RemoveTrailingLines())

    if remove_empty:
        pipeline.add(RemoveEmptyCell())

    if embed_images:
        pipeline.add(EmbedImages())

    if remove_output:
        pipeline.add(RemoveOutput())

    pipeline.add(JoinSource())

    return pipeline
