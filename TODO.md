- Parser and compilation:
    - Type:
        - if struct, parse for member called `base` to get parent type

    - templates: `template` `<` TypeName `>`
        - No need for TypeName definition: if someone uses a wrong type, the C compiler will take care of the errors.
            - This calls for documentation and standards

    - FunctionContents:
        - Variable definitions
        - foreach loops `for (G data: iterable)` -> `for (G *data = iterable.foreach(); data != NULL; data = iterable.foreach())`
        - method definitions: if member is not part of data struct `data.member(args)` -> `member(data, args)`, `data->member(args)` -> `member(*data, args)`
        - (CANCELLED) Automatic templates `List({1, 2, 3, 4})` -> `List<int>({1, 2, 3, 4})` because `{1, 2, 3, 4}` is `int[]`

    - Polymorphism:
        - Resolve base of type based on the `base` field of the class

    - NameSpaceContents:
        - member definitions: `namespace::member` -> `namespace_member` in all contexts
        - FunctionContents:
            - resolve colissions of names because of namespaces based on input types and their parent types.
            - resolve template calls and datatypes and request definition from `NameSpaceContents`
            - rename calls and datatypes to C names

- standard library:
    - String struct:
        - allocation
        - size
        - extension
        - reduction
        - iterable
        - get -> char
    - try/catch:
        - Exceptions/Errors:
            - Base struct:
                - const char[] name
                - string explanation
            - macro for quickly defining new Error: `ERROR(name)` -> Error struct
        